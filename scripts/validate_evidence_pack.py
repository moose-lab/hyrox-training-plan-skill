#!/usr/bin/env python3
"""Validate evidence-reference integrity for the HYROX Training Plan Skill."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
REFERENCES = ROOT / "references"

REQUIRED_JSON = [
    "training-principles.json",
    "periodization-models.json",
    "session-types.json",
    "race-standards.json",
    "pacing-strategy.json",
    "plan-template.json",
    "source-credibility.json",
    "multidomain-evidence.json",
]

REQUIRED_MARKDOWN = [
    "evidence-verification-notes.md",
    "expert-video-synthesis.md",
    "prompt-library.md",
]

VALID_LABELS = {
    "HYROX_DIRECT",
    "TRANSFER_EVIDENCE",
    "COACH_PRACTICE",
    "CLINICAL_REFERRAL",
}


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


def load_json(path: Path, errors: list[str]) -> dict[str, Any] | None:
    try:
        content = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        fail(errors, f"{path.relative_to(ROOT)}: invalid JSON ({exc})")
        return None
    if not isinstance(content, dict):
        fail(errors, f"{path.relative_to(ROOT)}: top-level object must be a JSON object")
        return None
    return content


def require_url(value: Any, field: str, pointer: str, errors: list[str]) -> None:
    if not isinstance(value, str) or not value.startswith("https://"):
        fail(errors, f"{pointer}: {field} must be a non-empty https URL")


def validate_multidomain(data: dict[str, Any], errors: list[str]) -> None:
    domains = data.get("domains")
    if not isinstance(domains, dict) or not domains:
        fail(errors, "references/multidomain-evidence.json: missing non-empty domains object")
        return

    for domain_name, domain in domains.items():
        pointer = f"references/multidomain-evidence.json.domains.{domain_name}"
        if not isinstance(domain, dict):
            fail(errors, f"{pointer}: must be an object")
            continue
        inputs = domain.get("required_inputs_before_personalization") or domain.get("required_inputs_before_education")
        if not isinstance(inputs, list) or not inputs:
            fail(errors, f"{pointer}: missing required intake inputs")
        guidance = domain.get("evidence_bounded_guidance")
        if not isinstance(guidance, list) or not guidance:
            fail(errors, f"{pointer}: missing evidence_bounded_guidance")
            continue
        for index, claim in enumerate(guidance):
            claim_pointer = f"{pointer}.evidence_bounded_guidance[{index}]"
            if not isinstance(claim, dict):
                fail(errors, f"{claim_pointer}: must be an object")
                continue
            for key in ("claim", "evidence_label", "operational_use", "do_not_infer"):
                if not isinstance(claim.get(key), str) or not claim[key].strip():
                    fail(errors, f"{claim_pointer}: missing non-empty {key}")
            label = claim.get("evidence_label")
            if label not in VALID_LABELS:
                fail(errors, f"{claim_pointer}: invalid evidence_label {label!r}")
            require_url(claim.get("source_url"), "source_url", claim_pointer, errors)
        flags = domain.get("referral_flags") or domain.get("clinical_referral_flags")
        if not isinstance(flags, list) or not flags:
            fail(errors, f"{pointer}: missing referral flags")


def validate_source_register(data: dict[str, Any], errors: list[str]) -> None:
    sources = data.get("operational_sources")
    if not isinstance(sources, dict):
        fail(errors, "references/source-credibility.json: missing operational_sources")
        return
    for group, entries in sources.items():
        if not isinstance(entries, list) or not entries:
            fail(errors, f"references/source-credibility.json.{group}: must be a non-empty list")
            continue
        for index, entry in enumerate(entries):
            pointer = f"references/source-credibility.json.{group}[{index}]"
            if not isinstance(entry, dict):
                fail(errors, f"{pointer}: must be an object")
                continue
            for key in ("id", "source_type" if group != "verified_expert_video_sources" else "speaker", "operational_use", "do_not_infer"):
                if not isinstance(entry.get(key), str) or not entry[key].strip():
                    fail(errors, f"{pointer}: missing non-empty {key}")
            url_key = "video_url" if group == "verified_expert_video_sources" else "url"
            require_url(entry.get(url_key), url_key, pointer, errors)


def main() -> int:
    errors: list[str] = []

    for filename in REQUIRED_JSON:
        path = REFERENCES / filename
        if not path.is_file():
            fail(errors, f"Missing required reference: references/{filename}")

    for filename in REQUIRED_MARKDOWN:
        path = REFERENCES / filename
        if not path.is_file() or not path.read_text(encoding="utf-8").strip():
            fail(errors, f"Missing or empty required reference: references/{filename}")

    multidomain = load_json(REFERENCES / "multidomain-evidence.json", errors)
    if multidomain is not None:
        validate_multidomain(multidomain, errors)

    source_register = load_json(REFERENCES / "source-credibility.json", errors)
    if source_register is not None:
        validate_source_register(source_register, errors)

    if errors:
        print("Evidence-pack validation FAILED:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Evidence-pack validation PASSED")
    print(f"Validated {len(REQUIRED_JSON)} JSON references and {len(REQUIRED_MARKDOWN)} Markdown references.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
