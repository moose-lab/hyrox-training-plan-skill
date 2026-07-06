# HYROX Training Plan Skill for Coding Agents

This repository provides a complete, science-based **HYROX Training Plan Skill** designed specifically for coding agents (such as Claude Code, Codex, Cursor, and Manus). By giving your agent access to this skill, you empower it to generate highly specific, physiologically sound daily training plans for athletes preparing for a HYROX fitness race.

## Repository Metadata

- Author: moose-lab
- Email: mooseindiehacker@gmail.com
- Repository: https://github.com/moose-lab/hyrox-training-plan-skill

## 🏃‍♂️ What is HYROX?

HYROX is a global fitness race combining 8 kilometers of running with 8 functional workout stations (SkiErg, Sled Push, Sled Pull, Burpee Broad Jumps, Rowing, Farmer's Carry, Sandbag Lunges, and Wall Balls). 

Unlike traditional CrossFit, HYROX is a **running-focused endurance event** (HIFT). Over 60% of the race is spent running. Therefore, training requires a fundamentally different approach—one rooted in endurance science, VO2max development, and specific compromised running practice, rather than maximum strength.

## 🧬 The Science Behind the Skill

This skill is not based on generic fitness advice. It is built upon a rigorous synthesis of:
1. **Academic Literature**: Including the 2025 *Frontiers in Physiology* study on HYROX performance determinants (which confirmed VO2max as the #1 predictor of success).
2. **Elite Coaching Methodologies**: Data extracted from 22 in-depth videos from world-class coaches and athletes (Rich Ryan, Dr. Dan Plews, Hunter McIntyre, and WOD Science).
3. **Official Race Standards**: Hardcoded weights, distances, and rules for all divisions (Open, Pro, Doubles, Relay).

The skill enforces 8 non-negotiable scientific constraints, ensuring that the generated plans avoid common pitfalls like the "Strength-First Trap" or the "Zone 3 Black Hole."

## 🛠️ How to Use This Skill with Your Agent

To use this skill, simply provide the contents of this repository to your coding agent. 

### Step 1: Provide Context
Point your agent to the `SKILL.md` file. This is the master instruction document that tells the agent how to use the rest of the files.

### Step 2: Request a Plan
Prompt your agent with your specific requirements. For example:
> *"I am an intermediate athlete competing in the Men's Open division in 12 weeks. I can train 6 days a week and have access to a full gym. Please use the HYROX Training Plan Skill to generate my 12-week daily training plan."*

### Step 3: Agent Execution
The agent will read the JSON reference files to:
- Establish the proper periodization (Base → Build → Peak → Taper).
- Select from the catalog of approved `session-types.json` (preventing hallucinated workouts).
- Apply the correct weights from `race-standards.json`.
- Ensure the plan meets the `training-principles.json` (e.g., ≥60% aerobic volume, 6+ hours between concurrent sessions).

### Step 4: Validation
You or the agent can run the included Python script to mathematically validate the generated plan against the core scientific principles:
```bash
python3 scripts/validate_plan.py path_to_generated_plan.json
```

## 📂 Repository Structure

- `SKILL.md`: The core prompt/instructions for the coding agent.
- `references/training-principles.json`: The 8 scientific constraints the agent must follow.
- `references/periodization-models.json`: Phase definitions and progression rules.
- `references/session-types.json`: The catalog of allowed running, strength, and HYROX-specific workouts.
- `references/race-standards.json`: Official weights and distances for all divisions.
- `scripts/validate_plan.py`: A script to validate the agent's output.

## 🎯 Goal: Build a Strong Body, Race Ready

By using this skill, you ensure your training is optimized for the specific metabolic demands of HYROX. You will build a robust aerobic engine, develop station-specific strength endurance, and master the art of running under fatigue—ultimately building a stronger, more resilient body for race day.

---
*Disclaimer: Always consult with a healthcare professional before beginning any high-intensity training program.*
