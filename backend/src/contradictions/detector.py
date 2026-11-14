"""Deterministic, high-precision contradiction checks across parsed case documents.

Each check compares an explicit FIR/structured value with what another document
states. The detector never decides which side is right; it only surfaces both.
"""

from __future__ import annotations

import re
from collections.abc import Iterable
from datetime import date, datetime

from ..domain.documents import DocumentType
from ..domain.parsed_documents import (
    FIR,
    CaseDiary,
    CCTVMetadata,
    Complaint,
    MedicalReport,
    ParsedDocument,
    PostmortemReport,
    SitePlan,
    SpotPanchnama,
    VehicleInspection,
    WitnessStatement,
)
from ..legal.ingredient_matcher import mentions
from ..text_normalization import name_tokens, normalize_for_match
from .models import Contradiction, ContradictionKind, ContradictionSeverity, ContradictionSide

INCIDENT_CUES = (
    "accident", "incident", "collision", "occurred", "happened", "attack", "assault", "stabbed", "robbed",
    "robbery", "theft", "crash", "hit", "fight", "fired", "shot", "snatched", "quarrel", "offence",
)
LATER_EVENT_CUES = (
    "reached", "arrived", "reported", "registered", "filed", "fir ", "hospital", "police station", "admitted",
    "recorded", "examined", "inspected", "seized", "arrested", "informed", "called",
)
DEATH_TERMS = ("died", "death", "deceased", "dead", "killed", "succumbed", "expired", "fatal")
SURVIVAL_TERMS = ("alive", "discharged", "conscious", "stable", "under treatment", "undergoing treatment", "recovering", "survived")
MONTHS = {m: i for i, m in enumerate(
    ["january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"], 1)}

_SENTENCE = re.compile(r"(?<=[.!?])\s+|\n+")
_TIME_COLON = re.compile(r"(?<!\d)(\d{1,2}):(\d{2})\s*(a\.?m\.?|p\.?m\.?|hrs|hours)?", re.IGNORECASE)
_TIME_MARKED = re.compile(r"(?<![\d:.])(\d{1,2})(?:\.(\d{2}))?\s*(a\.?m\.?|p\.?m\.?|hrs|hours)(?!\w)", re.IGNORECASE)
_DATE_ISO = re.compile(r"\b(\d{4})-(\d{2})-(\d{2})\b")
_DATE_DMY = re.compile(r"\b(\d{1,2})[/-](\d{1,2})[/-](\d{4})\b")
_DATE_TEXT = re.compile(
    r"\b(\d{1,2})(?:st|nd|rd|th)?\s+(january|february|march|april|may|june|july|august|september|october|november|december),?\s+(\d{4})\b",
    re.IGNORECASE,
)
_REGISTRATION = re.compile(r"\b[A-Z]{2}[ -]?\d{1,2}[ -]?[A-Z]{1,3}[ -]?\d{4}\b")


def _sentences(text: str | None) -> list[str]:
    return [s.strip() for s in _SENTENCE.split(text or "") if len(s.strip()) >= 12]


def _is_incident_sentence(sentence: str) -> bool:
    folded = sentence.casefold()
    return any(cue in folded for cue in INCIDENT_CUES) and not any(cue in folded for cue in LATER_EVENT_CUES)


def _clock_minutes(sentence: str) -> list[tuple[str, tuple[int, ...]]]:
    """Return (matched text, candidate minutes-since-midnight) for each clock time in the sentence."""

    found: list[tuple[str, tuple[int, ...]]] = []
    for regex in (_TIME_COLON, _TIME_MARKED):
        for match in regex.finditer(sentence):
            hour = int(match.group(1))
            minute = int(match.group(2) or 0)
            marker = (match.group(3) or "").lower().replace(".", "")
            if hour > 24 or minute > 59:
                continue
            if marker.startswith("p"):
                hour = hour % 12 + 12
            elif marker.startswith("a"):
                hour = hour % 12
            candidates = (hour * 60 + minute,)
            if not marker and hour <= 12:
                candidates = ((hour % 12) * 60 + minute, (hour % 12 + 12) * 60 + minute)
            found.append((match.group(0).strip(), candidates))
    return found


def _dates_in(sentence: str) -> list[tuple[str, date]]:
    found: list[tuple[str, date]] = []
    for match in _DATE_ISO.finditer(sentence):
        try:
            found.append((match.group(0), date(int(match.group(1)), int(match.group(2)), int(match.group(3)))))
        except ValueError:
            pass
    for match in _DATE_DMY.finditer(sentence):
        try:
            found.append((match.group(0), date(int(match.group(3)), int(match.group(2)), int(match.group(1)))))
        except ValueError:
            pass
    for match in _DATE_TEXT.finditer(sentence):
        try:
            found.append((match.group(0), date(int(match.group(3)), MONTHS[match.group(2).lower()], int(match.group(1)))))
        except ValueError:
            pass
    return found


def _label(document: ParsedDocument) -> str:
    kind = document.document_type.value.replace("_", " ").capitalize()
    for attribute in ("witness_name", "patient_name", "complainant_name"):
        name = getattr(document, attribute, None)
        if name:
            return f"{kind} ({name})"
    return kind


def _narratives(document: ParsedDocument) -> list[str]:
    if isinstance(document, FIR):
        return _sentences(document.narrative_text)
    if isinstance(document, Complaint):
        return _sentences(document.complaint_text)
    if isinstance(document, WitnessStatement):
        return _sentences(document.statement_text)
    if isinstance(document, CaseDiary):
        return [s for entry in document.entries for s in _sentences(entry.text)]
    if isinstance(document, (SpotPanchnama, VehicleInspection)):
        return [s for obs in document.observations for s in _sentences(obs)]
    if isinstance(document, MedicalReport):
        return [s for obs in (*document.observations, document.opinion_text or "") for s in _sentences(obs)]
    if isinstance(document, PostmortemReport):
        return [s for obs in (*document.findings, document.opinion_text or "", document.status or "") for s in _sentences(obs)]
    return []


def _side(document: ParsedDocument, text: str, value: str | None = None) -> ContradictionSide:
    return ContradictionSide(document_id=document.document_id, document_label=_label(document), text=text, value=value)


def _fmt_minutes(minutes: int) -> str:
    return f"{minutes // 60:02d}:{minutes % 60:02d}"


class ContradictionDetector:
    def detect(self, documents: Iterable[ParsedDocument]) -> tuple[Contradiction, ...]:
        docs = list(documents)
        findings: list[Contradiction] = []
        firs = [d for d in docs if isinstance(d, FIR)]
        for fir in firs:
            others = [d for d in docs if d is not fir]
            findings += self._time_and_date(fir, others)
            findings += self._vehicles(fir, others)
            findings += self._locations(fir, others)
            findings += self._people(fir, others)
        findings += self._life_status(docs)
        findings += self._chronology(docs, firs)
        order = {ContradictionSeverity.HIGH: 0, ContradictionSeverity.MEDIUM: 1, ContradictionSeverity.LOW: 2}
        return tuple(sorted(findings, key=lambda item: order[item.severity]))

    def _time_and_date(self, fir: FIR, others: list[ParsedDocument]) -> list[Contradiction]:
        found: list[Contradiction] = []
        occurrence = fir.occurrence_datetime
        if occurrence is None:
            return found
        has_time = (occurrence.hour, occurrence.minute) != (0, 0)
        fir_minutes = occurrence.hour * 60 + occurrence.minute
        for other in others:
            if isinstance(other, (MedicalReport, PostmortemReport)):
                continue
            for sentence in (s for s in _narratives(other) if _is_incident_sentence(s)):
                if has_time:
                    for text, candidates in _clock_minutes(sentence):
                        gap = min(min(abs(c - fir_minutes), 1440 - abs(c - fir_minutes)) for c in candidates)
                        if gap > 120:
                            found.append(
                                Contradiction(
                                    kind=ContradictionKind.TIME,
                                    severity=ContradictionSeverity.HIGH if gap > 360 else ContradictionSeverity.MEDIUM,
                                    summary=f"FIR places the incident at {_fmt_minutes(fir_minutes)}, but {_label(other)} states {text} (about {gap // 60}h {gap % 60}m apart).",
                                    why_it_matters="The time of occurrence anchors the prosecution timeline; a mismatch lets the defence challenge witness reliability.",
                                    sides=(_side(fir, f"FIR occurrence time: {occurrence:%Y-%m-%d %H:%M}", _fmt_minutes(fir_minutes)), _side(other, sentence, text)),
                                )
                            )
                            break
                for text, found_date in _dates_in(sentence):
                    delta = abs((found_date - occurrence.date()).days)
                    if delta >= 1:
                        found.append(
                            Contradiction(
                                kind=ContradictionKind.DATE,
                                severity=ContradictionSeverity.HIGH if delta > 7 else ContradictionSeverity.MEDIUM,
                                summary=f"FIR dates the incident {occurrence:%d %b %Y}, but {_label(other)} refers to {text}.",
                                why_it_matters="A different date of occurrence suggests the documents describe different events or contain an error that must be reconciled before filing.",
                                sides=(_side(fir, f"FIR occurrence date: {occurrence:%Y-%m-%d}", f"{occurrence:%Y-%m-%d}"), _side(other, sentence, text)),
                            )
                        )
                        break
        return found

    def _vehicles(self, fir: FIR, others: list[ParsedDocument]) -> list[Contradiction]:
        def registrations(document: ParsedDocument) -> set[str]:
            raw: list[str] = []
            for attribute in ("vehicle_registrations",):
                raw += list(getattr(document, attribute, ()) or ())
            single = getattr(document, "vehicle_registration", None)
            if single:
                raw.append(single)
            for sentence in _narratives(document):
                raw += _REGISTRATION.findall(sentence.upper())
            return {re.sub(r"[ -]", "", item.upper()) for item in raw if item}

        fir_regs = registrations(fir)
        if not fir_regs:
            return []
        found: list[Contradiction] = []
        for other in others:
            if isinstance(other, (MedicalReport, PostmortemReport)):
                continue
            other_regs = registrations(other)
            if other_regs and not (fir_regs & other_regs):
                found.append(
                    Contradiction(
                        kind=ContradictionKind.VEHICLE,
                        severity=ContradictionSeverity.MEDIUM,
                        summary=f"FIR records vehicle(s) {', '.join(sorted(fir_regs))}, but {_label(other)} records {', '.join(sorted(other_regs))}.",
                        why_it_matters="The vehicle is the link between the accused and the offence; unmatched registrations break that chain.",
                        sides=(_side(fir, f"FIR vehicles: {', '.join(sorted(fir_regs))}"), _side(other, f"{_label(other)} vehicles: {', '.join(sorted(other_regs))}")),
                    )
                )
        return found

    def _locations(self, fir: FIR, others: list[ParsedDocument]) -> list[Contradiction]:
        if not fir.occurrence_location:
            return []
        from rapidfuzz import fuzz

        found: list[Contradiction] = []
        for other in others:
            if isinstance(other, (SpotPanchnama, SitePlan, CCTVMetadata)) and other.location:
                score = fuzz.token_set_ratio(normalize_for_match(fir.occurrence_location), normalize_for_match(other.location))
                if score < 45:
                    found.append(
                        Contradiction(
                            kind=ContradictionKind.LOCATION,
                            severity=ContradictionSeverity.MEDIUM,
                            summary=f"FIR places the incident at '{fir.occurrence_location}', but {_label(other)} records '{other.location}'.",
                            why_it_matters="Place of occurrence determines jurisdiction and the scene evidence the court will rely on.",
                            sides=(_side(fir, f"FIR occurrence location: {fir.occurrence_location}", fir.occurrence_location), _side(other, f"{_label(other)} location: {other.location}", other.location)),
                        )
                    )
        return found

    def _people(self, fir: FIR, others: list[ParsedDocument]) -> list[Contradiction]:
        from rapidfuzz import fuzz

        def same_person(left: str, right: str) -> bool:
            a, b = " ".join(name_tokens(left)), " ".join(name_tokens(right))
            return bool(a and b) and fuzz.token_set_ratio(a, b) >= 80

        found: list[Contradiction] = []
        for other in others:
            if isinstance(other, Complaint) and fir.accused_names and other.person_complained_against_names:
                if not any(same_person(a, b) for a in fir.accused_names for b in other.person_complained_against_names):
                    found.append(
                        Contradiction(
                            kind=ContradictionKind.ACCUSED,
                            severity=ContradictionSeverity.HIGH,
                            summary=f"FIR names {', '.join(fir.accused_names)} as accused, but the complaint names {', '.join(other.person_complained_against_names)}.",
                            why_it_matters="Charging the wrong or an unestablished person is a fatal defect; the identity of the accused must be consistent across records.",
                            sides=(_side(fir, f"FIR accused: {', '.join(fir.accused_names)}"), _side(other, f"Complaint names: {', '.join(other.person_complained_against_names)}")),
                        )
                    )
            if isinstance(other, MedicalReport) and fir.victim_names and other.patient_name:
                if not any(same_person(v, other.patient_name) for v in fir.victim_names):
                    found.append(
                        Contradiction(
                            kind=ContradictionKind.VICTIM,
                            severity=ContradictionSeverity.MEDIUM,
                            summary=f"FIR names {', '.join(fir.victim_names)} as victim, but the medical report examined {other.patient_name}.",
                            why_it_matters="Injury evidence only proves the offence if it belongs to the named victim.",
                            sides=(_side(fir, f"FIR victim: {', '.join(fir.victim_names)}"), _side(other, f"Medical report patient: {other.patient_name}")),
                        )
                    )
        return found

    def _life_status(self, docs: list[ParsedDocument]) -> list[Contradiction]:
        medical = [d for d in docs if isinstance(d, (MedicalReport, PostmortemReport))]
        narrative_docs = [d for d in docs if isinstance(d, (FIR, Complaint, WitnessStatement, CaseDiary))]
        found: list[Contradiction] = []

        def first_sentence(document: ParsedDocument, terms: tuple[str, ...]) -> str | None:
            return next((s for s in _narratives(document) if mentions(s, terms)), None)

        survival = None
        for report in medical:
            if isinstance(report, PostmortemReport) and not report.is_applicable:
                survival = survival or (report, f"Post-mortem not applicable: {report.status or 'victim alive'}")
            elif first_sentence(report, SURVIVAL_TERMS) and not first_sentence(report, DEATH_TERMS):
                survival = survival or (report, first_sentence(report, SURVIVAL_TERMS))
        if survival:
            for document in narrative_docs:
                sentence = first_sentence(document, DEATH_TERMS)
                if sentence:
                    found.append(
                        Contradiction(
                            kind=ContradictionKind.LIFE_STATUS,
                            severity=ContradictionSeverity.HIGH,
                            summary=f"{_label(document)} describes a death, but {_label(survival[0])} indicates the victim survived.",
                            why_it_matters="Whether the victim died decides between culpable-homicide/murder sections and hurt/endangerment sections.",
                            sides=(_side(document, sentence), _side(survival[0], survival[1])),
                        )
                    )
                    break
        for report in medical:
            death_sentence = first_sentence(report, ("brought dead", "declared dead", "died", "succumbed", "cause of death"))
            if not death_sentence:
                continue
            for document in narrative_docs:
                injury = first_sentence(document, ("injured", "injury", "hurt", "grievous"))
                if injury and not first_sentence(document, DEATH_TERMS):
                    found.append(
                        Contradiction(
                            kind=ContradictionKind.LIFE_STATUS,
                            severity=ContradictionSeverity.MEDIUM,
                            summary=f"{_label(report)} records a death, but {_label(document)} describes only injuries.",
                            why_it_matters="The charge-sheet sections must match whether the victim died; the FIR may need amendment.",
                            sides=(_side(report, death_sentence), _side(document, injury)),
                        )
                    )
                    break
            break
        return found

    def _chronology(self, docs: list[ParsedDocument], firs: list[FIR]) -> list[Contradiction]:
        found: list[Contradiction] = []
        for fir in firs:
            if fir.occurrence_datetime is None:
                continue
            for document in docs:
                if isinstance(document, WitnessStatement) and document.statement_date and document.statement_date < fir.occurrence_datetime.date():
                    found.append(
                        Contradiction(
                            kind=ContradictionKind.CHRONOLOGY,
                            severity=ContradictionSeverity.HIGH,
                            summary=f"{_label(document)} is dated {document.statement_date:%d %b %Y}, before the incident on {fir.occurrence_datetime:%d %b %Y}.",
                            why_it_matters="A statement recorded before the incident cannot be genuine; this is an obvious line of attack in cross-examination.",
                            sides=(_side(fir, f"FIR occurrence date: {fir.occurrence_datetime:%Y-%m-%d}"), _side(document, f"Statement date: {document.statement_date:%Y-%m-%d}")),
                        )
                    )
        return found
