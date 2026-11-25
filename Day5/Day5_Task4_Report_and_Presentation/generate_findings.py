from pathlib import Path
import pandas as pd

# This script must be run from the repository root.
csv_path = Path("Day5/Day5_Task2_Exploratory_Analysis/employee_data.csv")
output_path = Path("Day5/Day5_Task4_Report_and_Presentation/report/Findings_Summary.md")

if not csv_path.exists():
    raise FileNotFoundError(
        f"Could not find {csv_path}. Keep the Task 2 and Task 4 folders "
        "inside the same Day5 folder, then run this script from the repository root."
    )

df = pd.read_csv(csv_path)
required = {"Department", "Age", "Monthly_Income"}
missing = required - set(df.columns)
if missing:
    raise ValueError(f"Dataset is missing required columns: {sorted(missing)}")

df["Age"] = pd.to_numeric(df["Age"], errors="coerce")
df["Monthly_Income"] = pd.to_numeric(df["Monthly_Income"], errors="coerce")
clean = df.dropna(subset=["Department", "Age", "Monthly_Income"]).copy()

# Insight 1: department income comparison
dept_income = clean.groupby("Department")["Monthly_Income"].mean().sort_values(ascending=False)
best_dept, best_income = dept_income.index[0], dept_income.iloc[0]
low_dept, low_income = dept_income.index[-1], dept_income.iloc[-1]

# Insight 2: age and income overview
mean_age = clean["Age"].mean()
median_income = clean["Monthly_Income"].median()

# Insight 3: attrition/overtime if these columns are present; otherwise use income spread.
attrition_col = next((c for c in clean.columns if c.lower() == "attrition"), None)
overtime_col = next((c for c in clean.columns if c.lower().replace("_", "").replace(" ", "") in
                     {"overtime", "overtimeflag", "overtimework"}), None)

third_insight = ""
recommendation_2 = ""
if attrition_col:
    attrition_rate = clean[attrition_col].astype(str).str.strip().str.lower().isin(
        ["yes", "1", "true", "left", "left the company"]
    ).mean() * 100
    third_insight = f"Overall attrition in the available records is **{attrition_rate:.1f}%**."
    recommendation_2 = (
        "Review exit reasons and retention risks using a larger, regularly updated employee "
        "dataset; use the observed attrition rate as a monitoring baseline."
    )
elif overtime_col:
    overtime_values = clean[overtime_col].astype(str).str.strip().str.lower()
    overtime_share = overtime_values.isin(["yes", "1", "true"]).mean() * 100
    third_insight = f"Employees marked as working overtime represent **{overtime_share:.1f}%** of the usable records."
    recommendation_2 = (
        "Review workload distribution and overtime patterns with department managers, "
        "then monitor whether workload changes improve employee outcomes."
    )
else:
    income_range = clean["Monthly_Income"].max() - clean["Monthly_Income"].min()
    third_insight = (
        f"Monthly income ranges from **{clean['Monthly_Income'].min():,.0f}** to "
        f"**{clean['Monthly_Income'].max():,.0f}** (range: **{income_range:,.0f}** currency units)."
    )
    recommendation_2 = (
        "Investigate the reasons for income differences across roles and departments before "
        "making compensation changes."
    )

recommendation_1 = (
    f"Review compensation and role structure in **{low_dept}**, whose average monthly income "
    f"({low_income:,.0f}) is below **{best_dept}** ({best_income:,.0f}); compare job levels and responsibilities "
    "before deciding on any adjustment."
)

summary = f"""# Employee Data Analysis – Findings Summary

## 1. Problem
The project explores employee information to understand workforce patterns, compare average monthly income across departments, and identify areas that may need management attention.

## 2. Data
The analysis uses the Task 2 employee CSV. The original file contains **{len(df)} rows** and **{len(df.columns)} columns**. After removing rows missing department, age, or monthly income, **{len(clean)} records** were used for the numeric comparisons. Monthly income is expressed in the dataset's currency units.

## 3. Three Key Insights
1. **Department income:** {best_dept} has the highest average monthly income (**{best_income:,.2f}**), while {low_dept} has the lowest (**{low_income:,.2f}**).
2. **Employee profile:** Average employee age is **{mean_age:.1f} years** and median monthly income is **{median_income:,.2f} currency units**.
3. **Workforce measure:** {third_insight}

## 4. Recommendations
1. {recommendation_1}
2. {recommendation_2}

## 5. Limitations
- The dataset is a small practice sample and may not represent the full workforce.
- The analysis is descriptive; it identifies patterns and does not prove cause and effect.
- Some fields may be missing or simplified, and monthly income currency is not explicitly specified in the dataset.
- Recommendations should be validated with HR context, role levels, employee feedback, and a larger dataset before real decisions are made.

---
*Generated from the Task 2 employee dataset. Review the findings and recommendations against your notebook outputs before submission.*
"""

output_path.parent.mkdir(parents=True, exist_ok=True)
output_path.write_text(summary, encoding="utf-8")
print(f"Summary created: {output_path}")
print(f"Rows in source data: {len(df)} | Rows used in numeric comparisons: {len(clean)}")
print("Review the generated summary before submitting it.")
