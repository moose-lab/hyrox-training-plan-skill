# Evidence Verification Notes

## Scope and Evidence-Label Method

Use the following labels in all skill references and generated outputs. **HYROX-direct** means an official HYROX standard or a study performed in HYROX athletes or a simulated HYROX format. **Transfer** means evidence from endurance, resistance, concurrent training, or athlete populations that may inform HYROX planning but is not proven specifically in HYROX. **Coach practice** means a credentialed coach or athlete's method extracted from a verified transcript; it must never be presented as causal scientific proof.

## Verified primary sources

### HYROX physiological demand and performance study

Brandt et al. (2025), *Frontiers in Physiology*, evaluated 11 recreational HYROX athletes in an Individual Open simulated competition. This small cross-sectional study found a median completion time of 86.5 minutes, with running taking 51.2 minutes and stations 32.8 minutes. Higher VO2max, greater endurance-training volume, and lower body-fat percentage correlated with faster completion. It provides **HYROX-direct association evidence**, not a universal causal prescription or population-level performance standard.

The study's practical recommendation was to emphasize endurance, use moderate-intensity training and HIIT, assign substantial training volume to running, and combine running with specific movements. It also advised caution about excessive running mileage and recognized the need for individualized programming. It does **not** establish a mandatory session percentage, universal heart-rate target, or individual lactate prescription.

Source: https://doi.org/10.3389/fphys.2025.1519240

### Athlete sleep consensus

Walsh et al. (2021), *British Journal of Sports Medicine*, recommends an individualized approach based on perceived sleep needs rather than a one-size-fits-all rule. The consensus identifies habitual sleep below 7 hours/night as a common marker of sleep inadequacy in athletes, recognizes that one full night without sleep reduces performance, and notes that evidence from partial sleep restriction and sleep-extension interventions is mixed and context dependent. It supports sleep education, screening, long-term habits, and managing travel and competition risks.

The skill may use sleep status as a **readiness flag** and recommend discussion with a clinician for persistent symptoms. It must not prescribe universal 9-hour targets, melatonin protocols, automated training cancellation, or diagnose insomnia.

Source: https://doi.org/10.1136/bjsports-2020-102025

### Nutrient timing position stand

Kerksick et al. (2017), International Society of Sports Nutrition, states that extended (>60 min) high-intensity exercise challenges fuel and fluid regulation, and describes a range of approximately 30-60 g carbohydrate per hour for relevant contexts. Total daily protein intake and evenly spaced feedings are emphasized more strongly than a narrow post-training window. Rapid glycogen restoration is only relevant when the next demanding session occurs within approximately 4 hours.

This is **transfer evidence** for HYROX. The skill must phrase pre-race, in-race, and recovery nutrition as test-in-training options rather than mandatory prescriptions. GI tolerance, diet history, event duration, sweat rate, comorbidities, and clinician/dietitian advice govern individual decisions.

Source: https://doi.org/10.1186/s12970-017-0189-4

### IOC supplement consensus

Maughan et al. (2018), *British Journal of Sports Medicine*, advises that only a small number of supplements have good supporting evidence in certain contexts; individual response varies and supplements should be trialled in training or simulated competition before use. It specifically warns of health risks and inadvertent anti-doping violations, and recommends a full nutritional assessment before decisions.

The skill may identify caffeine, creatine, nitrate, and buffering agents as **supplement topics requiring qualified individual review**, never as required HYROX interventions. It must ask about age, medications, health conditions, competing regulations, prior tolerance, and quality assurance before providing non-prescriptive educational details.

Source: https://doi.org/10.1136/bjsports-2018-099027

## Corrections to reject from unverified aggregations

Do not label 30-60 g/h carbohydrate, hydration/sodium ranges, or post-race macros as **HYROX-direct** evidence. Those recommendations are transfer evidence from endurance/position statements.

Do not encode the 10% volume rule, ACWR = 1.5, a fixed 6-8 hour separation, or a fixed deload interval as universal safety thresholds. These may be monitoring heuristics or coach practices, not validated automatic decision rules for individual HYROX athletes.

Do not encode blanket sleep targets, caffeine/melatonin rules, injury diagnoses, return-to-sport clearance, nor claims that a specific intervention prevents a particular injury. These require individualized assessment and often clinical input.

## Reference design implications

Every rule added to the skill must record: `claim`, `evidence_label`, `source_url`, `source_type`, `population_or_context`, `operational_use`, and `do_not_infer`.

The agent must cite direct and transfer evidence separately in plan rationales, and ask rather than assume when medical history, supplement use, dietary restrictions, injury, pregnancy, medications, or sleep disorder symptoms can affect the advice.

## References

1. Brandt T, Ebel C, Lebahn C, Schmidt A. Acute physiological responses and performance determinants in Hyrox. *Front Physiol*. 2025. https://doi.org/10.3389/fphys.2025.1519240
2. Walsh NP, et al. Sleep and the athlete: narrative review and 2021 expert consensus recommendations. *Br J Sports Med*. 2021. https://doi.org/10.1136/bjsports-2020-102025
3. Kerksick CM, et al. International society of sports nutrition position stand: nutrient timing. *J Int Soc Sports Nutr*. 2017. https://doi.org/10.1186/s12970-017-0189-4
4. Maughan RJ, et al. IOC consensus statement: dietary supplements and the high-performance athlete. *Br J Sports Med*. 2018. https://doi.org/10.1136/bjsports-2018-099027

*This document supports educational plan-generation workflows and does not replace individualized medical, nutrition, or sports-medicine care.*
