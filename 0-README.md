# ============================================================
# SleepImpact  –  Full Analysis Script
# ============================================================
# 0. Imports
# ------------------------------------------------------------
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import pearsonr, spearmanr, ttest_ind
import statsmodels.api as sm
import os

plt.rcParams["figure.dpi"] = 110           # clearer plots

# ------------------------------------------------------------
# 1. Load & initial clean-up
# ------------------------------------------------------------
FILE = "dsa 210 term project (2).xlsx"     # <- adjust if needed
df   = pd.read_excel(FILE)

df.columns = df.columns.str.strip()
df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

num_cols = [
    "Caffeine (mg)", "Social Media Usage (minutes)",
    "Cigarettes", "Step Count",
    "Sleep Onset Time (minutes)", "Sleep Quality"
]
df[num_cols] = df[num_cols].apply(pd.to_numeric, errors="coerce")

# drop user-flagged anomaly days if an “Anomaly” column exists
if "Anomaly" in df.columns:
    df = df[df["Anomaly"].isna()]

# fill numeric gaps with column means
df[num_cols] = df[num_cols].fillna(df[num_cols].mean(numeric_only=True))

# ------------------------------------------------------------
# 2. Feature engineering / enrichment
# ------------------------------------------------------------
# scale fixes
df["Steps_k"]     = df["Step Count"] / 1_000                        # steps in thousands
df["SleepOnset_h"] = df["Sleep Onset Time (minutes)"] / 60          # minutes → hours

# caffeine dose per kg (if weight info exists)
if "Weight" in df.columns:
    df["Caf_per_kg"] = df["Caffeine (mg)"] / df["Weight"]

# caffeine bucket (Low / Med / High by terciles)
df["Caf_Level"] = pd.qcut(df["Caffeine (mg)"],
                          q=[0, .33, .66, 1.0],
                          labels=["Low", "Med", "High"])

# high-screen dummy (top 25 %)
q75 = df["Social Media Usage (minutes)"].quantile(.75)
df["SM_High"] = (df["Social Media Usage (minutes)"] >= q75).astype(int)

# z-scores for numeric predictors
for col in ["Caffeine (mg)", "Social Media Usage (minutes)",
            "Cigarettes", "Step Count"]:
    df[col + "_z"] = (df[col] - df[col].mean()) / df[col].std()

# 7-day rolling mean of sleep-onset (minutes)
df = df.sort_values("Date")
df["SleepOnset_7d_avg"] = (df["Sleep Onset Time (minutes)"]
                           .rolling(window=7, min_periods=1).mean())

# weekend indicator
df["IsWeekend"] = (df["Date"].dt.weekday >= 5).astype(int)

print("Feature-engineered columns:", df.columns[-10:].tolist())

# ------------------------------------------------------------
# 3. Exploratory Data Analysis (EDA)
# ------------------------------------------------------------
print("\n=== Descriptive statistics ===")
print(df.describe(include='all').T)

plt.figure(figsize=(9,7))
sns.heatmap(df[num_cols].corr(), annot=True, cmap="coolwarm", linewidths=.5)
plt.title("Correlation matrix"); plt.tight_layout(); plt.show()

def scatter(x, y, **kw):
    plt.figure(figsize=(8,6))
    sns.scatterplot(x=x, y=y, data=df, **kw)
    plt.xlabel(x); plt.ylabel(y); plt.title(f"{x} vs {y}")
    plt.tight_layout(); plt.show()

scatter("Caffeine (mg)", "Sleep Onset Time (minutes)")
scatter("Social Media Usage (minutes)", "Sleep Onset Time (minutes)")
scatter("Cigarettes", "Sleep Quality")
scatter("Step Count", "Sleep Quality")

# sleep trend line
plt.figure(figsize=(10,6))
plt.plot(df["Date"], df["Sleep Quality"], marker="o", label="Sleep Quality")
plt.plot(df["Date"], df["SleepOnset_7d_avg"], marker="s", label="Sleep Onset 7-day avg (min)")
plt.legend(); plt.xticks(rotation=45); plt.title("Sleep metrics over time")
plt.tight_layout(); plt.show()

# ------------------------------------------------------------
# 4. Hypothesis testing
# ------------------------------------------------------------
targets    = ["Sleep Onset Time (minutes)", "Sleep Quality"]
predictors = ["Caffeine (mg)", "Social Media Usage (minutes)",
              "Cigarettes", "Step Count"]

print("\n=== Pearson & Spearman tests ===")
for tgt in targets:
    for pred in predictors:
        r, p  = pearsonr(df[pred], df[tgt])
        ρ, p2 = spearmanr(df[pred], df[tgt])
        print(f"{pred:30} → {tgt:27}  Pearson r={r:6.3f}  p={p:.3f} | Spearman ρ={ρ:6.3f}  p={p2:.3f}")

# two-sample t-test (high vs low caffeine) on sleep onset
median_caf = df["Caffeine (mg)"].median()
hi_onset   = df[df["Caffeine (mg)"] >= median_caf]["Sleep Onset Time (minutes)"]
lo_onset   = df[df["Caffeine (mg)"] <  median_caf]["Sleep Onset Time (minutes)"]
t_stat, p_val = ttest_ind(hi_onset, lo_onset, equal_var=False)
print(f"\nT-test: high vs low caffeine — sleep onset  t={t_stat:.2f}, p={p_val:.3f}")

# ------------------------------------------------------------
# 5. Multiple regression (Sleep Onset) with engineered features
# ------------------------------------------------------------
X = df[["Caffeine (mg)", "Social Media Usage (minutes)",
        "Cigarettes", "Step Count", "IsWeekend"]]
X = sm.add_constant(X)
y = df["Sleep Onset Time (minutes)"]

model = sm.OLS(y, X).fit()
print("\n=== Multiple regression summary ===")
print(model.summary())

# ------------------------------------------------------------
# 6. Export artefacts (optional)
# ------------------------------------------------------------
df.to_csv("sleepimpact_processed.csv", index=False)
df[num_cols].corr().to_csv("sleepimpact_corr_matrix.csv")
print("\nOutput saved: sleepimpact_processed.csv & sleepimpact_corr_matrix.csv")
print("Working dir :", os.getcwd())
