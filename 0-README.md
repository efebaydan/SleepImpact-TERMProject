# SleepImpact – DSA 210 Term Project

## Project Overview
This project examines how four everyday habits—**caffeine intake, social-media use, cigarette smoking, and physical activity (step count)**—shape two critical sleep outcomes:
- **Sleep-onset time** (minutes required to fall asleep)  
- **Sleep quality** (subjective 1–10 rating plus Sleep Cycle’s objective score)

Data was collected automatically from **Sleep Cycle**, **iPhone Focus Time**, and **Apple Health**.  
Through exploratory visualisation and statistical testing, the aim is to identify which behaviour changes yield the biggest improvements in sleep.

---

## Objectives
1. **Map Sleep Influencers:** Quantify links between each habit and the two sleep metrics.
2. **Highlight Key Drivers:** Determine which variables matter most, then prioritize them for change.
3. **Deliver Actionable Advice:** Translate findings into clear, data-backed recommendations.
4. **Practice Data-Science Skills:** Apply EDA, hypothesis testing, regression, and visualization techniques from DSA 210 to an authentic problem.

---

## Motivation
- **Personal Growth:** Consistently better sleep should boost health, mood, and academic focus.
- **Evidence over Guesswork:** Replace anecdotes (“coffee keeps me up”) with verified numbers.
- **Low-Friction Logging:** All metrics are already tracked by apps I use daily—no extra effort.
- **Broader Relevance:** Insights on screen-time, caffeine, and exercise can benefit productivity and well-being beyond sleep.

---

## Dataset
| Field           | Description                              |
|-----------------|------------------------------------------|
| **Date**        | Record date                              |
| **Caffeine (mg)** | Total intake                          |
| **Social Media Usage (minutes)** | Focus-Time screen minutes |
| **Cigarettes**  | Number smoked that day                   |
| **Step Count**  | Apple Health steps                       |
| **Sleep Onset Time (minutes)** | Minutes to fall asleep     |
| **Sleep Quality** | 1–10 self-rating & Sleep Cycle %       |

> Days affected by illness, travel, or exams are flagged and can be excluded.

---

## Tools & Technologies
Python · Pandas · Matplotlib / Seaborn · SciPy / Statsmodels · scikit-learn · Jupyter Notebook

---

## Analysis Plan
1. **Ingest & Clean:** Load daily logs, resolve missing values, drop anomalies, standardize units.
2. **Visual Exploration:** Scatterplots, heatmaps and time-series to reveal preliminary patterns.
3. **Hypothesis Testing:** See next section.
4. **Trend Analysis:** Track month-to-month drift and 7-day rolling averages to capture gradual change.

---

## Hypothesis Testing
| No. | Null Hypothesis (H₀)                     | Alternative (H₁)                       | Test & α            |
|-----|------------------------------------------|----------------------------------------|---------------------|
| 1   | Caffeine has no linear association with sleep-onset time. | Higher caffeine **increases** sleep-onset time. | Pearson & Spearman correlation (α = 0.05) |
| 2   | Daily screen-time does not affect sleep quality. | Heavy screen-time **reduces** sleep quality. | Two-sample *t*-test: High vs Low quartiles |
| 3   | Cigarette count is uncorrelated with sleep quality. | More cigarettes **lower** sleep quality. | Pearson/Spearman correlation |
| 4   | Step count has no effect on sleep-onset or quality. | More steps **improve** sleep metrics. | Linear regression: Sleep ~ Steps + covariates |

> If any p-value < 0.05, the null hypothesis (H₀) was rejected for that test.

---

## Feature Engineering
To enrich the dataset, a new binary feature “High_SocialMedia” was created. Days with social media use above the median were labeled as 1 (“High”), and others as 0 (“Low”). This engineered variable was used as an additional predictor in machine learning models.

---

## Machine Learning Model
A logistic regression model was trained to predict whether sleep quality was “High” or “Low” (above or below the median) using daily habits and the engineered “High_SocialMedia” feature. Model accuracy and confusion matrix were reported to evaluate performance.

---

## Illustrative Analyses
- **Caffeine vs Sleep-Onset:** scatterplot and Pearson *r*
- **Screen-Time Bins vs Sleep Quality:** boxplot + *t*-test
- **Step-Count Quartiles:** sleep-quality distribution across activity levels
- **Smoothed Time-Series:** 7-day rolling curves for onset and quality

---

## Results & Interpretation  

| Habit         | Statistical Result                                    | Interpretation                                          |
|---------------|------------------------------------------------------|---------------------------------------------------------|
| **Screen-Time** | High-screen days score –0.4 pt lower on sleep quality (*t* = 2.1, p ≈ 0.04) | Evening phone use measurably harms perceived restfulness → consider a screen curfew. |
| **Caffeine**    | *r* ≈ +0.15 with sleep-onset, p = 0.75 (ns)         | ≤ 2 cups/day shows no detectable delay; monitor if intake increases. |
| **Cigarettes**  | *r* ≈ –0.28 with sleep quality, p = 0.19 (ns)       | Suggests poorer sleep on smoking days, but sample too small for firm proof. |
| **Step Count**  | Slope ≈ –0.6 min per 1 000 steps, p = 0.66          | More activity may shorten time to fall asleep, though effect is weak so far. |
| **ML Model**    | Logistic regression accuracy ≈ 0.72, confusion matrix shown in script | Predictive modeling suggests that social media use and step count help classify sleep quality. |

> **Summary:** Screen-time appears to be the most influential—and modifiable—factor. Expanding the dataset (>60 days) will clarify the roles of caffeine, cigarettes, and physical activity.

---

## Limitations and Future Work
- Dataset covers a short time window; longer tracking may clarify weaker effects.
- Additional features (e.g., bedtime consistency, diet, stress) could be incorporated.
- The ML model could be improved with more data and alternative algorithms.

---
## AI Usage Statement

This project used OpenAI ChatGPT-4 for guidance on:
- Report structuring
- Feature engineering and machine learning implementation (scikit-learn syntax)
- Example prompts:
    - "How do I add a logistic regression model to classify sleep quality using pandas and scikit-learn?"
    - "How can I explain feature engineering steps in a data science report?"

All code and analysis were reviewed and adapted by the author.




