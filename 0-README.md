# SleepImpact-DSA210Project

## Project Overview
Over the next three months, I’ll analyse how four daily habits—**caffeine intake, social-media usage, cigarette smoking, and physical activity (step count)**—affect **sleep-onset time** and **sleep quality**.  
Data come from **Sleep Cycle** (sleep metrics), **iPhone Focus Time** (screen-time), and **Apple Health** (step count).  
By visualising patterns and running statistical tests, I’ll discover which lifestyle tweaks produce measurable improvements in sleep.

---

## Objectives
1. **Understand Sleep Influencers**  
   Quantify the relationship between caffeine, screen-time, cigarettes, steps and sleep metrics.
2. **Identify Key Factors**  
   Detect which variables matter most, then design targeted habit changes.
3. **Data-Driven Optimisation**  
   Turn insights into actionable guidelines to improve sleep quality.
4. **Apply Data-Science Skills**  # SleepImpact-DSA210Project

## Project Overview
Over the next three months I’ll analyse how four daily habits—**caffeine intake, social-media usage, cigarette smoking, and physical activity (step count)**—affect two key outcomes:

* **Sleep-onset time** (minutes it takes to fall asleep)  
* **Sleep quality** (1-10 self-rating + Sleep Cycle %)

Data come from  
* **Sleep Cycle** – sleep metrics  
* **iPhone Focus Time** – screen-time minutes  
* **Apple Health** – step count  

By visualising patterns and running statistical tests I’ll discover which lifestyle tweaks produce measurable improvements in sleep.

---

## Objectives
1. **Understand Sleep Influencers**  
   Quantify the relationship between caffeine, screen-time, cigarettes, steps and sleep metrics.  
2. **Identify Key Factors**  
   Detect which variables matter most, then design targeted habit changes.  
3. **Data-Driven Optimisation**  
   Turn insights into actionable guidelines to improve sleep quality.  
4. **Apply Data-Science Skills**  
   Use DSA 210 methods (EDA, hypothesis testing, regression, visualisation) on real-world data.  

---

## Motivation
- **Personal Growth** – Better sleep → better health, mood and academic performance.  
- **Scientific Approach** – Replace gut feeling with objective, data-backed decisions.  
- **Practical Application** – All metrics are passively tracked by apps I already use.  
- **Long-Term Impact** – Findings may generalise to productivity, stress management, etc.  

---

## Dataset
| Field | Description |
|-------|-------------|
| **Date** | Day of record |
| **Caffeine (mg)** | Daily caffeine consumed |
| **Social-Media Usage (min)** | Focus-Time screen minutes |
| **Cigarettes** | Number smoked that day |
| **Step Count** | Apple Health steps |
| **Sleep-Onset (min)** | Minutes to fall asleep |
| **Sleep Quality** | 1–10 self-rating + Sleep Cycle % |

*Anomaly days — illness, travel, exams — are flagged and can be excluded from analysis.*

---

## Tools and Technologies
Python · Pandas · Matplotlib / Seaborn · SciPy / Statsmodels · Jupyter Notebook

---

## Analysis Plan
1. **Data Collection & Preparation**  
    • Import daily logs into a Pandas DataFrame.  
    • Handle missing values, standardise units, drop anomaly days.  

2. **Visualisation**  
    • Scatter plots, heat-maps and time-series to explore relationships.  
    • Example: *Caffeine (mg) vs Sleep-Onset (min)* scatter.  

3. **Hypothesis Testing**  
    • **H₀:** Habits do **not** affect sleep-onset or quality.  
    • **H₁:** One or more habits **do** affect sleep-onset or quality.  
    • Pearson / Spearman correlations, two-sample *t*-tests, multiple-linear regression.  

4. **Trend Analysis**  
    • Examine month-to-month drift and 7-day rolling averages.  
    • Assess how changes in screen-time or step count track with sleep quality.  

---

## Example Analyses
- **Caffeine vs Sleep-Onset Scatter** – upward slope would suggest caffeine delays sleep.  
- **High- vs Low Screen-Time Boxplot** – tests if heavy phone days lower quality.  
- **Step-Count Quartiles** – boxplot of sleep quality across activity levels.  
- **7-Day Rolling Metrics** – line chart of smoothed sleep-onset & quality over time.  

---

## Findings & Interpretation  
*(results reflect the current 30-day dataset; rerun notebook after adding new records)*

| Habit Variable | Statistical Result | Interpretation |
|----------------|--------------------|----------------|
| **Screen-Time** | High-screen days show **–0.4 pt** lower sleep-quality (t = 2.1, *p* ≈ 0.04) | Late-night scrolling measurably harms perceived restfulness → set a phone curfew. |
| **Caffeine** | Pearson *r* ≈ +0.15 with sleep-onset, *p* = 0.75 (ns) | Two-cup-per-day range didn’t delay sleep; effect might appear only at larger doses. |
| **Cigarettes** | *r* ≈ –0.28 with sleep-quality, *p* = 0.19 (ns) | Trend towards poorer sleep on smoking days, but sample size is too small for significance. |
| **Step Count** | Regression slope ≈ –0.6 min per 1 000 steps (*p* = 0.66) | More activity may shorten sleep-onset slightly, though effect is weak at current activity levels. |

> **Overall:** Among the four habits, **screen-time** is the clearest actionable lever in the pilot data. Extending data collection (> 60 days) will increase statistical power for caffeine, cigarettes and step count.

---

## Conclusion
By the end of the project I aim to answer:

- Which habit has the **strongest** impact on sleep?  
- Can small, data-driven tweaks (e.g., screen curfew) measurably boost quality?  
- Is screen-time or caffeine more disruptive?  
- How can these insights turn into everyday actions for better rest?  

*Beyond improving my own sleep, this project showcases the power of data-driven decision-making in daily life.*

   Use DSA 210 methods (EDA, hypothesis testing, regression, visualisation) on real-world data.

---

## Motivation
- **Personal Growth** – Better sleep → better health, mood and academic performance.  
- **Scientific Approach** – Replace gut-feeling with objective, data-backed decisions.  
- **Practical Application** – All metrics are passively tracked by apps I already use.  
- **Long-Term Impact** – Findings may generalise to productivity, stress-management, etc.

---

## Dataset
| Field | Description |
|-------|-------------|
| **Date** | Day of record |
| **Caffeine (mg)** | Daily caffeine consumed |
| **Social-Media Usage (min)** | Focus-Time screen minutes |
| **Cigarettes** | Number smoked that day |
| **Step Count** | Apple Health steps |
| **Sleep-Onset (min)** | Minutes to fall asleep |
| **Sleep Quality** | 1–10 self-rating + Sleep Cycle % |

*Anomaly days (illness, travel, exams) are flagged and can be excluded.*

---

## Tools and Technologies
Python · Pandas · Matplotlib / Seaborn · SciPy / Statsmodels · Jupyter Notebook

---

## Analysis Plan
1. **Data Collection & Preparation**  
2. **Visualisation** (scatter, heat-map, time-series)  
3. **Hypothesis Testing** (correlation tests, t-tests, multiple regression)  
4. **Trend Analysis** (rolling averages, month-to-month change)

---

## Example Analyses
- Caffeine vs Sleep-Onset scatter  
- Boxplot: High vs Low Screen-Time ➜ Sleep Quality  
- Step-Count quartiles vs Sleep Quality  
- 7-day rolling Sleep metrics trend

---

## Findings & Interpretation  *(based on pilot data — will update as dataset grows)*
| Habit | Key statistical result | Practical interpretation |
|-------|-----------------------|--------------------------|
| **Caffeine** | *r* ≈ +0.15 with sleep-onset, *p* = 0.75 (ns) | Two cups/day range is **not** enough to delay sleep measurably. Larger doses may be needed before an effect shows. |
| **Screen-Time** | High-screen days ↓ sleep quality by ≈ 0.4 pts (t = 2.1, *p* ≈ 0.04) | Late-night scrolling **does** hurt perceived restfulness; instituting a phone curfew could pay off. |
| **Cigarettes** | *r* ≈ -0.28 with sleep quality, *p* = 0.19 | Trend suggests smokers’ sleep feels worse, but sample is too small for significance. |
| **Step Count** | Regression slope ≈ -0.59 min/1 000 steps (ns) | More activity might shorten sleep-onset slightly; effect small at current activity levels. |

> **Overall:** Screen-time emerges as the clearest actionable lever; caffeine and steps show weak/insignificant effects in the current 4-week window. Collecting > 60 days of data will increase power.

---

## Conclusion
By the end of this project I aim to answer:

- Which daily habit has the **strongest** impact on sleep?  
- Can small, data-driven tweaks (e.g., screen curfew) measurably boost quality?  
- Is screen-time or caffeine more disruptive?  
- How can these insights turn into daily actions for better rest?

*This project demonstrates how everyday digital traces can guide evidence-based habit changes for healthier sleep.*
