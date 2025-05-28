import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import pearsonr, spearmanr, linregress, ttest_ind
import statsmodels.api as sm
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix
import os

plt.rcParams["figure.dpi"] = 110  # Sharper plots

# ============================================================
# 1 — LOAD & CLEAN DATA
# ============================================================
FILE = "dsa 210 term project (2).xlsx"  # <-- Update path/name if needed
df = pd.read_excel(FILE)

df.columns = df.columns.str.strip()  # Remove stray spaces
df["Date"] = pd.to_datetime(df["Date"])  # Parse date column

num_cols = [
    "Caffeine (mg)", "Social Media Usage (minutes)", "Cigarettes",
    "Step Count", "Sleep Onset Time (minutes)", "Sleep Quality"
]
df[num_cols] = df[num_cols].apply(pd.to_numeric, errors="coerce")
df[num_cols] = df[num_cols].fillna(df[num_cols].mean(numeric_only=True))

print(f">> Shape: {df.shape},  Missing numeric cells filled.")

# ============================================================
# 2 — DESCRIPTIVE STATS & CORRELATION MATRIX
# ============================================================
print("\n=== Descriptive Statistics ===")
print(df[num_cols].describe().T)

plt.figure(figsize=(9, 7))
sns.heatmap(df[num_cols].corr(), annot=True, cmap="coolwarm", linewidths=.5)
plt.title("Correlation Matrix")
plt.tight_layout()
plt.show()

# ============================================================
# 3 — VISUALIZATIONS
# ============================================================
def scatter(x, y, xlabel=None, ylabel=None, title=None):
    """Quick scatter-plot helper."""
    plt.figure(figsize=(8, 6))
    sns.scatterplot(x=x, y=y, data=df)
    plt.xlabel(xlabel or x)
    plt.ylabel(ylabel or y)
    plt.title(title or f"{x} vs {y}")
    plt.tight_layout()
    plt.show()

scatter("Caffeine (mg)", "Sleep Onset Time (minutes)",
        "Caffeine (mg)", "Sleep onset (min)", "Caffeine vs Sleep Onset")

scatter("Social Media Usage (minutes)", "Sleep Onset Time (minutes)",
        "Social media (min)", "Sleep onset (min)", "Social Media vs Sleep Onset")

scatter("Cigarettes", "Sleep Quality",
        "Cigarettes / day", "Sleep quality (1-10)", "Cigarettes vs Sleep Quality")

scatter("Step Count", "Sleep Quality",
        "Steps", "Sleep quality (1-10)", "Steps vs Sleep Quality")

# Time series of sleep metrics
plt.figure(figsize=(10, 6))
plt.plot(df["Date"], df["Sleep Quality"], marker="o", label="Sleep Quality")
plt.plot(df["Date"], df["Sleep Onset Time (minutes)"], marker="s", label="Sleep Onset (min)")
plt.title("Sleep Metrics Over Time")
plt.xlabel("Date")
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# ============================================================
# 4 — HYPOTHESIS TESTING
# ============================================================
targets = ["Sleep Onset Time (minutes)", "Sleep Quality"]
predictors = ["Caffeine (mg)", "Social Media Usage (minutes)", "Cigarettes", "Step Count"]

print("\n=== Pearson & Spearman Correlation Tests ===")
for tgt in targets:
    for pred in predictors:
        pr, pp = pearsonr(df[pred], df[tgt])
        sr, sp = spearmanr(df[pred], df[tgt])
        print(f"{pred:30} → {tgt:27} | Pearson r={pr:6.3f} p={pp:.3f} "
              f"| Spearman ρ={sr:6.3f} p={sp:.3f}")

# Example t-test: high vs low caffeine on sleep onset
median_caf = df["Caffeine (mg)"].median()
hi_onset = df[df["Caffeine (mg)"] >= median_caf]["Sleep Onset Time (minutes)"]
lo_onset = df[df["Caffeine (mg)"] < median_caf]["Sleep Onset Time (minutes)"]
t_stat, p_val = ttest_ind(hi_onset, lo_onset, equal_var=False)
print(f"\nT-test: High vs Low Caffeine — Sleep Onset: t={t_stat:.2f}, p={p_val:.3f}")

# ============================================================
# 5 — MULTIPLE REGRESSION (Sleep Onset)
# ============================================================
X = df[["Caffeine (mg)", "Social Media Usage (minutes)", "Cigarettes", "Step Count"]]
X = sm.add_constant(X)
y = df["Sleep Onset Time (minutes)"]

model = sm.OLS(y, X).fit()
print("\n=== Multiple Regression: Sleep Onset ~ Daily Habits ===")
print(model.summary())

# ============================================================
# 6 — EXPORT CORRELATION MATRIX (optional)
# ============================================================
corr_path = "sleep_corr_matrix.csv"
df[num_cols].corr().to_csv(corr_path)
print(f"\nCorrelation matrix saved to '{corr_path}'.")
print("Working directory:", os.getcwd())

# ============================================================
# 7 — FEATURE ENGINEERING & MACHINE LEARNING TASK
# ============================================================
# Create a binary column for high social media usage
median_smu = df["Social Media Usage (minutes)"].median()
df["High_SocialMedia"] = (df["Social Media Usage (minutes)"] > median_smu).astype(int)

# Categorize sleep quality as high/low (based on median)
median_quality = df["Sleep Quality"].median()
df["SleepQuality_Class"] = (df["Sleep Quality"] > median_quality).astype(int)  # 1=High, 0=Low

# Logistic Regression to predict sleep quality class
X_ml = df[["Caffeine (mg)", "Cigarettes", "Step Count", "High_SocialMedia"]]
y_ml = df["SleepQuality_Class"]

X_train, X_test, y_train, y_test = train_test_split(X_ml, y_ml, test_size=0.25, random_state=42)
model_lr = LogisticRegression()
model_lr.fit(X_train, y_train)
y_pred = model_lr.predict(X_test)

# Results
acc = accuracy_score(y_test, y_pred)
cm = confusion_matrix(y_test, y_pred)
print(f"\nLogistic Regression Accuracy: {acc:.2f}")
print("Confusion Matrix:\n", cm)
