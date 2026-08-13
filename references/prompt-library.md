# Prompt Library for Coding Agents

Use these prompts after loading `SKILL.md` and the references it names. Replace bracketed text only with user-provided information. Each prompt explicitly limits the agent to educational and planning support rather than medical or dietetic prescription.

## 1. Daily Session Generator

```text
Use the HYROX Training Plan Skill to create today’s session for [division] in the [Base/Build/Peak/Taper] phase. Athlete context: [recent sessions, sleep trend, soreness/stress, pain status, equipment, time available].

First check whether any clinical-referral flags apply. If yes, do not diagnose or prescribe; explain the referral boundary and offer only a conservative, non-clinical planning alternative if appropriate. If no flag applies, prescribe one session with warm-up, main work, technique cues, cool-down, objective load, RPE/pace cue, and one modification option.

For every rationale, label it HYROX_DIRECT, TRANSFER_EVIDENCE, or COACH_PRACTICE. Cite the source file and source URL. Do not invent data, fixed heart-rate zones, supplement doses, or medical claims.
```

## 2. Twelve-Week Race Plan Generator

```text
Use the HYROX Training Plan Skill to produce a 12-week plan for [division] with [sessions/week], [race date], [current running/strength baseline], [target], [equipment], and [time constraints].

Read training-principles.json, race-standards.json, periodization-models.json, session-types.json, plan-template.json, and multidomain-evidence.json. Use Base → Build → Peak → Taper, but explain all phase-duration adjustments. Include at least one lower-stress option and an athlete-readiness adjustment rule.

Separate HYROX_DIRECT findings from TRANSFER_EVIDENCE and COACH_PRACTICE. Include a non-prescriptive fueling-practice workflow and sleep/readiness checks, not a supplement protocol. Return valid JSON conforming to the example plan schema and validate it with scripts/validate_plan.py.
```

## 3. Nutrition Education Companion

```text
Create an evidence-bounded HYROX nutrition education companion for [session/race context]. Ask first for body mass if needed, dietary preferences, GI tolerance, expected duration, prior race-fueling experience, medical conditions, medication, pregnancy/postpartum status, and whether a sports dietitian is involved.

If a clinical or dietetic referral flag exists, do not provide a personalized protocol. Otherwise, explain food/fluid/carbohydrate practice options using TRANSFER_EVIDENCE labels, state that products must be tested in training, and list what the athlete should record (food, timing, fluid, GI response, perceived energy). Do not make a universal grams-per-hour target, sodium target, calorie floor, or brand recommendation.
```

## 4. Sleep and Readiness Adjustment

```text
Use the HYROX Training Plan Skill to adjust [today/this week] based on [7-14 day sleep trend], [stress], [soreness], [session-RPE], [travel], and [pain status].

Treat sleep as a trend-based readiness input, not a diagnosis. If persistent sleep symptoms, significant daytime sleepiness, chest symptoms, altered gait, or worsening pain are present, raise CLINICAL_REFERRAL and do not create a hard training prescription. Otherwise offer: (a) proceed as planned, (b) lower-impact substitute, or (c) reduced-volume alternative. Label each rationale with evidence type and cite Walsh et al. 2021 where sleep evidence is used.
```

## 5. Coach-Video Research Ingestion

```text
Evaluate this source before adding it to the HYROX Training Plan Skill: [video URL/article URL]. Verify author/speaker credential, retrieve and inspect the transcript or full text, and capture the exact claim, timestamp/page, source URL, population/context, and commercial relationship.

Classify every proposed insight as HYROX_DIRECT, TRANSFER_EVIDENCE, COACH_PRACTICE, or UNSUPPORTED_OPINION. State what cannot be inferred. Do not add it as a hard rule unless it is supported by a high-quality primary source or consensus statement and its applicability is explicit.
```

## 6. Source-Quality Audit

```text
Audit every claim in this proposed HYROX plan: [plan text or JSON]. For each claim, identify its evidence label, source URL, source type, population/context, operational use, and do-not-infer boundary. Flag uncited numerical targets, universal claims, medical/nutrition/supplement prescriptions, and coaching anecdotes presented as proof. Rewrite flagged content into safe, evidence-bounded language.
```

## Reference Method

Each new claim must be stored with this minimum record:

```json
{
  "claim": "Plain-language statement",
  "evidence_label": "HYROX_DIRECT | TRANSFER_EVIDENCE | COACH_PRACTICE | CLINICAL_REFERRAL",
  "source_title": "Full title",
  "source_url": "https://...",
  "source_type": "original study | systematic review | consensus | verified transcript",
  "population_or_context": "Who/what was studied",
  "operational_use": "How an agent may use it",
  "do_not_infer": "What the agent must not claim"
}
```

A claim without a traceable source URL and a stated `do_not_infer` boundary must not enter the production references.
