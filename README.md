# HYROX Training Plan Skill for Coding Agents

**HYROX Training Plan Skill** is an open, evidence-bounded package for coding agents such as Claude Code, Codex, Cursor, and Manus. It helps an agent generate structured daily HYROX training plans, maintain correct race standards, and communicate training, nutrition, sleep, recovery, and supplement content without presenting coaching anecdotes or adjacent research as universal medical facts.

The project is designed for athletes preparing for HYROX and for developers building tools that support that preparation. It does **not** replace a qualified coach, registered sports dietitian, physician, physiotherapist, or sports-medicine professional.

## Why the Skill Is Evidence-Bounded

HYROX combines 8 km of running with eight prescribed functional stations. A 2025 simulated Individual Open study of 11 recreational HYROX athletes found that running represented more time than the stations and that higher VO2max and greater endurance-training volume were associated with faster completion. The small study supports an endurance emphasis, but it does not prove a single program, fixed training split, or universal physiological target.[1]

> **Core principle:** every output distinguishes what is directly supported in HYROX, what is transferred from neighboring endurance/strength research, and what is a coach’s practical method.

| Evidence label | Meaning | How an agent may use it |
|---|---|---|
| `HYROX_DIRECT` | Official standard or research performed in HYROX/simulated HYROX settings | State the population, finding, and limitation. |
| `TRANSFER_EVIDENCE` | Relevant evidence from endurance, strength, nutrition, sleep, or concurrent training | Explain that it informs, but does not prove, HYROX programming. |
| `COACH_PRACTICE` | Method found in a verified credentialed coach/athlete transcript | Offer it as an individualized experiment, not a hard rule. |
| `CLINICAL_REFERRAL` | Medical, injury, dietetic, sleep-disorder, medication, or supplement-risk situation | Do not prescribe; recommend appropriate qualified care. |

## Research Foundation

The repository has a primary-source layer and a practical coaching layer. The primary layer includes the HYROX performance study, athlete sleep consensus, sports-nutrition position statement, IOC supplement consensus, load-management work, and injury-prevention evidence.[1] [2] [3] [4] [5] [6] The coaching layer audits professional videos from Dr Dan Plews, RMR Training, WOD Science, and Triage Nutrition. Each video entry records transcript availability, speaker credentials, claims, commercial-bias flags, and what an agent must **not** infer.

| Domain | Included contribution | Boundary enforced by the skill |
|---|---|---|
| Training | Race standards, periodization, session catalogue, progression guardrails | No universal volume, heart-rate, lactate, or taper rule. |
| Nutrition | Fueling-practice workflow and recovery-nutrition education | No diagnosis, calorie-floor formula, universal grams-per-hour target, or brand recommendation. |
| Sleep and recovery | Trend-based readiness checks and low-impact alternatives | No wearable-based diagnosis, universal sleep target, or automatic cancellation after one poor night. |
| Load and injury risk | Progressive exposure, variation, and review triggers | No injury prediction from a fixed 10% rule, ACWR cutoff, or single metric. |
| Supplements | Evidence/risk education and anti-doping guardrails | No default supplement regimen, mandatory product, or individualized dosing. |

## Installation

Clone the repository and give your coding agent access to `SKILL.md` and the `references/` directory.

```bash
git clone https://github.com/moose-lab/hyrox-training-plan-skill.git
cd hyrox-training-plan-skill
```

The repository is released under the [MIT License](LICENSE). It can be adapted for personal, coaching, or product-development workflows, provided you retain the evidence boundaries and do not present the generated output as medical or dietetic care.

## Use with a Coding Agent

Ask the agent to read `SKILL.md` before it writes a plan. The skill then tells it which references to load for race standards, periodization, training constraints, nutrition, sleep, recovery, and expert-video practices.

```text
Use the HYROX Training Plan Skill in this repository to create a 12-week plan.

Athlete context: Individual Open; race in 12 weeks; four running sessions and two gym sessions available; current running volume is 25 km/week; full HYROX equipment available; no current pain; sleep is usually 7–8 hours; no known dietary restrictions.

Label every rationale HYROX_DIRECT, TRANSFER_EVIDENCE, or COACH_PRACTICE. Include a readiness-adjustment option and a fueling-practice option. Do not provide medical, dietetic, or supplement prescriptions. Produce JSON matching the example schema, then validate it.
```

The agent should collect race format, timeline, current load, training history, equipment, availability, readiness, pain status, and relevant nutrition/supplement context before claiming to personalize a plan. Missing information should lead to conservative assumptions and explicit questions, not invented precision.

## Validate a Generated Plan

Use the included validator to catch structural and programming-guardrail errors.

```bash
python3 scripts/validate_evidence_pack.py
python3 scripts/validate_plan.py examples/sample-12-week-plan.json
python3 scripts/validate_plan.py path/to/generated-plan.json
```

A passing result means the JSON passes the repository’s automated checks; it does **not** establish that the plan is safe, individualized, medically suitable, or optimal for a specific athlete.

## Repository Structure

```text
├── SKILL.md                               # Core operating instructions for coding agents
├── examples/
│   └── sample-12-week-plan.json           # Validated JSON plan example
├── references/
│   ├── training-principles.json            # Core programming constraints
│   ├── periodization-models.json           # Base → Build → Peak → Taper scaffold
│   ├── session-types.json                  # Workout catalogue
│   ├── race-standards.json                 # Official format and division standards
│   ├── pacing-strategy.json                # Pacing/transition reference
│   ├── plan-template.json                  # Input and output schema
│   ├── multidomain-evidence.json           # Nutrition, sleep, recovery, injury, supplement boundaries
│   ├── expert-video-synthesis.md           # Transcript-audited expert methods
│   ├── evidence-verification-notes.md      # Primary-source audit and limitations
│   ├── prompt-library.md                   # Reusable prompts for coding agents
│   └── source-credibility.json             # Source-evaluation record
└── scripts/
    ├── validate_plan.py                    # Plan-structure validator
    ├── validate_evidence_pack.py           # Reference-integrity validator
    └── discover_expert_videos.py           # YouTube candidate discovery utility
```

## Add New Knowledge Safely

Do not paste social-media claims directly into a reference JSON. Use the [source-validation prompt](references/prompt-library.md#5-coach-video-research-ingestion) and store each claim with a source URL, source type, population/context, evidence label, operational use, and `do_not_infer` boundary. The detailed format is in [prompt-library.md](references/prompt-library.md#reference-method).

Professional video content is valuable for practical questions—such as station technique, session structure, and how elite athletes sequence work—but it has a different evidentiary role than a peer-reviewed study. The repository intentionally preserves that difference.

## Health and Scope Notice

High-intensity training, race fueling, sleep concerns, injuries, medicines, pregnancy/postpartum status, and supplements can require individualized professional assessment. Seek care promptly for chest pain, fainting, acute injury, pain that changes gait, persistent sleep disturbance, persistent gastrointestinal symptoms, or other concerning symptoms. Athletes subject to anti-doping rules should obtain qualified guidance before using supplements.

## References

[1] Brandt T, Ebel C, Lebahn C, Schmidt A. [Acute physiological responses and performance determinants in HYROX](https://doi.org/10.3389/fphys.2025.1519240). *Frontiers in Physiology*. 2025.

[2] Kerksick CM, et al. [International society of sports nutrition position stand: nutrient timing](https://doi.org/10.1186/s12970-017-0189-4). *Journal of the International Society of Sports Nutrition*. 2017.

[3] Walsh NP, et al. [Sleep and the athlete: narrative review and 2021 expert consensus recommendations](https://doi.org/10.1136/bjsports-2020-102025). *British Journal of Sports Medicine*. 2021.

[4] Maughan RJ, et al. [IOC consensus statement: dietary supplements and the high-performance athlete](https://doi.org/10.1136/bjsports-2018-099027). *British Journal of Sports Medicine*. 2018.

[5] Gabbett TJ. [Load Management: What It Is and What It Is Not!](https://doi.org/10.1177/19417381231179946). *Sports Health*. 2023.

[6] Lauersen JB, Andersen TE, Andersen LB. [Strength training as superior, dose-dependent and safe prevention of acute and overuse sports injuries](https://doi.org/10.1136/bjsports-2018-099078). *British Journal of Sports Medicine*. 2018.
