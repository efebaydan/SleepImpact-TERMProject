# SleepImpact – DSA 210 Term Project

## Project Overview
During the next three months I will examine how four everyday habits—**caffeine intake, social-media use, cigarette smoking, and physical activity (step count)**—shape two critical sleep outcomes:

* **Sleep-onset time** ∙ minutes required to fall asleep  
* **Sleep quality** ∙ subjective 1–10 rating plus Sleep Cycle’s objective score  

Data will be collected automatically from **Sleep Cycle**, **iPhone Focus Time**, and **Apple Health**.  
Through exploratory visualisation and rigorous statistical testing, I aim to identify which behaviour changes yield the biggest improvements in sleep.

---

## Objectives
1. **Map Sleep Influencers** Quantify links between each habit and the two sleep metrics.  
2. **Highlight Key Drivers** Determine which variables matter most, then prioritise them for change.  
3. **Deliver Actionable Advice** Translate findings into clear, data-backed recommendations.  
4. **Practise Data-Science Skills** Apply EDA, hypothesis testing, regression, and visualisation techniques from DSA 210 to an authentic problem.

---

## Motivation
- **Personal Growth** Consistently better sleep should boost health, mood, and academic focus.  
- **Evidence over Guesswork** Replace anecdotes (“coffee keeps me up”) with verified numbers.  
- **Low-Friction Logging** All metrics are already tracked by apps I use daily—no extra effort.  
- **Broader Relevance** Insights on screen-time, caffeine, and exercise can benefit productivity and well-being beyond sleep.

---

## Dataset
| Field | Description |
|-------|-------------|
| **Date** | Record date |
| **Caffeine (mg)** | Total intake |
| **Social-Media (min)** | Focus-Time screen minutes |
| **Cigarettes** | Number smoked that day |
| **Step Count** | Apple Health steps |
| **Sleep-Onset (min)** | Minutes to fall asleep |
| **Sleep Quality** | 1–10 self-rating & Sleep Cycle % |

> *Days affected by illness, travel, or exams are flagged and can be excluded.*

---

## Tools & Technologies
Python · Pandas · Matplotlib / Seaborn · SciPy / Statsmodels · Jupyter Notebook  

---

## Analysis Plan
1. **Ingest & Clean** Load daily logs, resolve missing values, drop anomalies, standardise units.  
2. **Visual Exploration** Scatterplots, heat-maps and time-series to reveal preliminary patterns.  
3. **Hypothesis Testing** see next section.  
4. **Trend Analysis** Track month-to-month drift and 7-day rolling averages to capture gradual change.

---

## Hypothesis Testing
| No. | Null Hypothesis (H₀) | Alternative (H₁) | Test & α |
|-----|----------------------|------------------|----------|
| 1 | Caffeine has no linear association with sleep-onset time. | Higher caffeine **increases** sleep-onset time. | Pearson & Spearman correlation (α = 0.05) |
| 2 | Daily screen-time does not affect sleep quality. | Heavy screen-time **reduces** sleep quality. | Two-sample *t*-test: High vs Low quartiles |
| 3 | Cigarette count is uncorrelated with sleep quality. | More cigarettes **lower** sleep quality. | Pearson/Spearman correlation |
| 4 | Step count has no effect on sleep-onset or quality. | More steps **improve** sleep metrics. | Linear regression: Sleep ~ Steps + covariates |

> If any p-value < 0.05, we will reject H₀ for that relationship.  
> Multiple comparison corrections (Benjamini–Hochberg) will be applied to avoid false positives.

---

## Illustrative Analyses
- **Caffeine vs Sleep-Onset** ∙ scatterplot and Pearson *r*.  
- **Screen-Time Bins vs Sleep Quality** ∙ boxplot + *t*-test.  
- **Step-Count Quartiles** ∙ sleep-quality distribution across activity levels.  
- **Smoothed Time-Series** ∙ 7-day rolling curves for onset and quality.

---

## Findings & Interpretation*  
*(current 30-day sample; rerun notebook after logging new data)*  

| Habit | Statistical Result | Interpretation |
|-------|--------------------|----------------|
| **Screen-Time** | High-screen days score **–0.4 pt** lower on sleep quality (*t* = 2.1, p ≈ 0.04) | Evening phone use measurably harms perceived restfulness → institute a screen curfew. |
| **Caffeine** | *r* ≈ +0.15 with sleep-onset, p = 0.75 (ns) | ≤ 2 cups/day shows no detectable delay; monitor if intake increases. |
| **Cigarettes** | *r* ≈ –0.28 with sleep quality, p = 0.19 (ns) | Suggests poorer sleep on smoking days, but sample too small for firm proof. |
| **Step Count** | Slope ≈ –0.6 min per 1 000 steps, p = 0.66 | More activity may shorten time to fall asleep, though effect is weak so far. |

> **Summary:** Screen-time currently appears to be the most influential—and modifiable—factor. Expanding the dataset (> 60 days) will clarify the roles of caffeine, cigarettes, and physical activity.

---

## Conclusion
By project’s end I intend to know:

* Which habit most strongly alters sleep.  
* Whether simple interventions (e.g., 22:00 phone curfew) produce tangible gains.  
* Whether caffeine or screen-time is the bigger disruptor.  
* How to translate statistical insights into daily routines for reliably better rest.

*Ultimately, this project demonstrates the value of data-driven decision-making in everyday life—starting with a better night’s sleep.*
