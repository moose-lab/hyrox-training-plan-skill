---
name: hyrox-training-plan
description: "Generate science-based HYROX training plans. Use for: creating customized training programs for HYROX athletes across all divisions (Open, Pro, Doubles, Relay), applying proper periodization, and structuring weekly microcycles based on verified exercise physiology principles."
---

# HYROX Training Plan Generator

This skill equips you to act as an elite HYROX coach and generate highly specific, science-based training plans. The methodology is synthesized from 22 top YouTube coaching videos (Rich Ryan, Dan Plews, WOD Science, Hunter McIntyre) and academic literature (Frontiers in Physiology, 2025).

## Core Philosophy

HYROX is **NOT** CrossFit. It is a 60-90 minute running-focused endurance event (HIFT) where >60% of the time is spent running. 
The #1 predictor of finish time is VO2max. Maximum strength is poorly correlated with success.
**Do not generate plans that prioritize heavy lifting over aerobic capacity.**

## Required References

Before generating a plan, you MUST read the relevant reference files:

1. `references/training-principles.json` - The 8 non-negotiable constraints (Read FIRST)
2. `references/periodization-models.json` - How to structure the Base → Build → Peak → Taper phases
3. `references/session-types.json` - The exact workouts to prescribe (Do not invent random workouts)
4. `references/race-standards.json` - The exact weights and distances for the user's specific division

## Workflow for Generating a Plan

When a user requests a HYROX training plan:

### Step 1: Gather Requirements
Determine the following from the user (ask if missing):
- **Division**: Open, Pro, Doubles, or Relay (Men/Women/Mixed)
- **Current Fitness Level**: Beginner, Intermediate, Advanced
- **Time Available**: Weeks until race (8-16 recommended) and sessions per week (4-10)
- **Equipment Access**: Do they have sleds, ergs, etc.?

### Step 2: Establish the Periodization Framework
Read `periodization-models.json` and map out the phases based on total weeks:
- Base Phase (~30%): Focus on Zone 2 running and general strength
- Build Phase (~40%): Add threshold runs and compromised running
- Peak Phase (~20%): Race pace and specific transitions
- Taper Phase (~10%): Volume reduction

*Rule: Include a deload week (30% volume reduction) every 3-4 weeks.*

### Step 3: Design the Microcycles (Weekly Schedule)
Read `plan-template.json` for weekly structure templates and `session-types.json` for specific workouts.
- Ensure ≥60% of total volume is aerobic (Zone 1-2).
- Ensure at least one `RUN_THRESHOLD` session per week during Build/Peak.
- Ensure at least one `RUN_COMPROMISED` session per week during Build/Peak.
- Ensure strength sessions are separated from hard endurance by ≥6 hours.

### Step 4: Apply Division Standards
Read `race-standards.json` to assign the correct weights for sleds, farmer's carry, lunges, and wall balls.
- Base phase: 60-70% of race weight
- Build phase: Progress to 100% of race weight
- Peak phase: 100% of race weight

### Step 5: Format the Output
Generate the final plan in a clear, structured format (Markdown or JSON depending on user request).
Include the rationale behind the programming, citing the principles from `training-principles.json`.

## Validation

If generating a JSON plan programmatically, you can validate it against the core principles using:
```bash
python3 /home/ubuntu/skills/hyrox-training-plan/scripts/validate_plan.py <path_to_plan.json>
```

## Anti-Patterns to Avoid
- **Strength-First Trap**: Programming heavy 1RM lifting. Focus on strength-endurance instead.
- **Simulation Overload**: Programming full HYROX simulations every week. Maximum is once every 3-4 weeks.
- **Zone 3 Black Hole**: Too much unstructured moderate intensity. Keep easy days easy (Zone 2) and hard days hard (Zone 4).
- **Neglecting Running**: Failing to program at least 3-4 dedicated running sessions per week.
