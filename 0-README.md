# SleepImpact – DSA 210 Term Project

## Project Overview  
During the next three months I will examine how four everyday habits—**caffeine intake, social-media use, cigarette smoking, and physical activity (step count)**—shape two critical sleep outcomes:

* **Sleep-onset time** ∙ minutes needed to fall asleep  
* **Sleep quality** ∙ subjective 1-10 rating plus Sleep Cycle’s objective score  

Data will be collected automatically from **Sleep Cycle**, **iPhone Focus Time**, and **Apple Health**.  
Through exploratory visualisation and rigorous statistical testing, I aim to identify which behaviour changes yield the biggest improvements in sleep.

---

## Objectives  
1. **Map Sleep Influencers** Quantify links between each habit and the two sleep metrics.  
2. **Highlight Key Drivers** Discover which variables matter most and prioritise them for change.  
3. **Deliver Actionable Advice** Translate findings into clear, data-backed recommendations.  
4. **Practise Data-Science Skills** Apply EDA, hypothesis testing, regression, and visualisation techniques from DSA 210 to an authentic problem.

---

## Motivation  
* **Personal Growth** Consistently better sleep should boost health, mood, and academic focus.  
* **Evidence over Guesswork** Replace anecdotes (“coffee keeps me up”) with verified numbers.  
* **Low-Friction Logging** All metrics are already tracked by apps I use daily—no extra effort.  
* **Broader Relevance** Insights on screen-time, caffeine, and exercise can benefit productivity and well-being beyond sleep.

---

## Dataset  
| Field | Description |
|-------|-------------|
| **Date** | Record date |
| **Caffeine (mg)** | Total intake |
| **Social-Media (min)** | Focus-Time screen minutes |
| **Cigarettes** | Count per day |
| **Step Count** | Apple Health steps |
| **Sleep-Onset (min)** | Minutes to fall asleep |
| **Sleep Quality** | Self-rating (1-10) and Sleep Cycle % |

> *Days affected by illness, travel, or exams are flagged and may be excluded from analysis.*

---

## Tools & Technologies  
Python · Pandas · Matplotlib / Seaborn · SciPy / Statsmodels · Jupyter Notebook  

---

## Analysis Plan  
1. **Ingest & Clean** Load daily logs, resolve missing values, drop anomalies, standardise units.  
2. **Visual Exploration** Scatterplots, heat-maps, and time-series to reveal preliminary patterns.  
3. **Hypothesis Testing**  
   * **H₀** Habits do **not** influence sleep-onset or quality.  
   * **H₁** At least one habit **does** influence these outcomes.  
   Pearson/Spearman correlations, two-sample *t*-tests, and multiple linear regression will be used.  
4. **Trend Analysis** Track month-to-month drift and 7-day rolling averages to capture gradual change.

---

## Illustrative Analyses  
* **Caffeine vs Sleep-Onset** ∙ scatterplot and Pearson *r*  
* **Screen-Time Bins vs Sleep Quality** ∙ box-and-whisker + *t*-test  
* **Step-Count Quartiles** ∙ sleep-quality distribution across activity levels  
* **Smoothed Time-Series** ∙ 7-day rolling curves for onset and quality

---

## Findings & Interpretation*  
*(current 30-day sample; update after additional data are logged)*  

| Habit | Key Statistic | Practical Takeaway |
|-------|---------------|--------------------|
| **Screen-Time** | High-screen days score **0.4 points lower** on sleep quality (*t* = 2.1, *p* ≈ 0.04) | Reducing evening phone use should immediately improve perceived restfulness. |
| **Caffeine** | Weak correlation with sleep-onset (*r* ≈ 0.15, *p* = 0.75) | ≤ 2 cups/day shows no measurable delay; monitor if intake rises. |
| **Cigarettes** | Trend towards lower quality (*r* ≈ -0.28, *p* = 0.19) | Likely detrimental, but current dataset too small for firm proof. |
| **Step Count** | Slope ≈ -0.6 min per 1 000 steps (*p* = 0.66) | More steps may shorten time to fall asleep, but effect is modest. |

> **Summary:** Screen-time is the most reliable lever so far. A larger sample (> 60 days) will clarify caffeine, cigarette, and activity effects.

---

## Conclusion  
By project’s end I will know:

* Which habit most strongly alters sleep.  
* Whether simple changes (e.g., a 22:00 screen curfew) produce tangible gains.  
* Whether caffeine or screen-time is the bigger disruptor.  
* How to convert statistical insights into everyday routines for consistently better rest.

*Ultimately, this project will demonstrate the value of data-driven decision-making in everyday life—starting with a better night’s sleep.*  
