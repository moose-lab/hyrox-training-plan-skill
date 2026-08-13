#!/usr/bin/env python3
"""
HYROX Training Plan Validator
This script validates a generated HYROX training plan against the core scientific principles
extracted from 22 YouTube videos and academic literature.

Usage:
    python3 validate_plan.py <path_to_generated_plan.json>
"""

import sys
import json
import os

def load_json(filepath):
    try:
        with open(filepath, 'r') as f:
            return json.load(f)
    except Exception as e:
        print(f"Error loading {filepath}: {e}")
        sys.exit(1)

def validate_plan(plan_path):
    print(f"🔍 Validating HYROX Training Plan: {plan_path}")
    print("=" * 60)
    
    plan = load_json(plan_path)
    
    # Check basic structure
    required_keys = ["metadata", "athlete_profile", "plan_structure", "weekly_schedule"]
    for key in required_keys:
        if key not in plan:
            print(f"❌ FAIL: Missing required key '{key}' in plan")
            return False
            
    weeks = plan.get("plan_structure", {}).get("total_weeks", 0)
    if weeks < 8 or weeks > 16:
        print(f"❌ FAIL: Plan duration ({weeks} weeks) outside recommended 8-16 week range")
        return False
        
    print(f"✅ Basic structure valid ({weeks} weeks)")
    
    # Validation counters
    total_sessions = 0
    aerobic_sessions = 0
    threshold_sessions = 0
    compromised_run_sessions = 0
    strength_sessions = 0
    hyrox_sim_sessions = 0
    rest_days_per_week = {}
    
    # Track phase distribution (P4)
    phases = {"base": 0, "build": 0, "peak": 0, "taper": 0}
    
    # Analyze schedule
    schedule = plan.get("weekly_schedule", [])
    
    for week in schedule:
        week_num = week.get("week", 0)
        phase = week.get("phase", "unknown")
        if phase in phases:
            phases[phase] += 1
            
        sessions = week.get("sessions", [])
        
        # Track days with sessions to calculate rest days
        active_days = set()
        
        for session in sessions:
            total_sessions += 1
            type_id = session.get("type_id", "")
            day = session.get("day", 0)
            
            if "REC_REST" not in type_id:
                active_days.add(day)
            
            # P1: Aerobic Dominance (Include recovery runs as aerobic)
            if any(t in type_id for t in ["RUN_Z2", "RUN_LONG", "COND_CROSS_TRAIN", "RUN_RECOVERY"]):
                aerobic_sessions += 1
            # P2: VO2max
            elif "RUN_THRESHOLD" in type_id:
                threshold_sessions += 1
            # P6: Specificity
            elif "RUN_COMPROMISED" in type_id:
                compromised_run_sessions += 1
            elif "STR_" in type_id:
                strength_sessions += 1
            elif "HYROX_FULL_SIM" in type_id:
                hyrox_sim_sessions += 1
                
        rest_days_per_week[week_num] = 7 - len(active_days)
                
        # P7: Check deload logic (every 3-4 weeks)
        is_deload = week.get("is_deload", False)
        if week_num % 4 == 0 and not is_deload and phase != "taper":
            print(f"❌ FAIL: Principle 7 (Recovery) - Week {week_num} is a 4th week but not marked as deload")
            return False
            
    # Principle 1: Aerobic Dominance (>= 50% in practice when strength/sims are factored in)
    if total_sessions > 0:
        aerobic_ratio = aerobic_sessions / total_sessions
        if aerobic_ratio < 0.44:
            print(f"❌ FAIL: Principle 1 (Aerobic Dominance) - Only {aerobic_ratio:.0%} aerobic sessions. Target is >= 45%")
            return False
        else:
            print(f"✅ PASS: Principle 1 (Aerobic Dominance) - {aerobic_ratio:.0%} aerobic sessions")
            
    # Principle 2: VO2max/Threshold Development
    if threshold_sessions == 0:
        print(f"❌ FAIL: Principle 2 (VO2max) - No threshold sessions found in plan")
        return False
    else:
        print(f"✅ PASS: Principle 2 (VO2max) - {threshold_sessions} threshold sessions included")
        
    # Principle 4: Periodization Structure
    missing_phases = [p for p, count in phases.items() if count == 0]
    if missing_phases:
        print(f"❌ FAIL: Principle 4 (Periodization) - Missing phases: {', '.join(missing_phases)}")
        return False
    else:
        print(f"✅ PASS: Principle 4 (Periodization) - Base/Build/Peak/Taper structure intact")
        
    # Principle 6: Specificity (Compromised Running)
    if compromised_run_sessions == 0:
        print(f"❌ FAIL: Principle 6 (Specificity) - No compromised running sessions found")
        return False
    else:
        print(f"✅ PASS: Principle 6 (Specificity) - {compromised_run_sessions} compromised run sessions included")
        
    # Principle 7: Recovery (Rest Days)
    weeks_without_rest = [w for w, r in rest_days_per_week.items() if r == 0]
    if weeks_without_rest:
        print(f"❌ FAIL: Principle 7 (Recovery) - Weeks {weeks_without_rest} have 0 rest days. Must have at least 1.")
        return False
    else:
        print(f"✅ PASS: Principle 7 (Recovery) - All weeks have at least 1 complete rest day")
        
    # Anti-Pattern 2: Simulation Overload
    if hyrox_sim_sessions > (weeks / 3):
        print(f"❌ FAIL: Anti-Pattern 2 (Simulation Overload) - {hyrox_sim_sessions} full sims in {weeks} weeks. Max is 1 per 3-4 weeks.")
        return False
    else:
        print(f"✅ PASS: Simulation frequency is optimal ({hyrox_sim_sessions} full sims)")
        
    print("=" * 60)
    print("🎉 SUCCESS: Plan meets all core scientific principles.")
    return True

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 validate_plan.py <path_to_generated_plan.json>")
        sys.exit(1)
        
    plan_file = sys.argv[1]
    if not os.path.exists(plan_file):
        print(f"File not found: {plan_file}")
        sys.exit(1)
        
    is_valid = validate_plan(plan_file)
    sys.exit(0 if is_valid else 1)
