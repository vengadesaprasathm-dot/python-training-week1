from pathlib import Path
import pandas as pd

# Keep input and output files in the same folder as this Python script.
FOLDER = Path(__file__).resolve().parent
input_file = FOLDER / "sales_data.csv"
output_file = FOLDER / "clean_data.csv"

# 1. Load the original dataset.
df = pd.read_csv(input_file)

# 2. Record the before-cleaning statistics.
before_rows = len(df)
before_missing = int(df.isna().sum().sum())
before_duplicates = int(df.duplicated().sum())

# 3. Standardise text: remove extra spaces and use consistent title case.
for column in ["Customer", "City", "Category"]:
    df[column] = df[column].astype("string").str.strip().str.title()

# 4. Fix data types.
df["Age"] = pd.to_numeric(df["Age"], errors="coerce")
df["Sales"] = pd.to_numeric(df["Sales"], errors="coerce")
df["Order_Date"] = pd.to_datetime(df["Order_Date"], errors="coerce")

# 5. Handle missing values with a reason for each column.
# Order_ID: keep as the row identifier; do not invent an ID if missing.
# Customer: leave missing and flag it if it occurs (no reliable value to infer).
# Age: fill missing values with the median because age is numeric and may be skewed.
# City: leave missing and flag it if it occurs (location cannot be safely guessed).
# Sales: fill missing values with the median because sales are numeric and can contain outliers.
# Order_Date: leave missing and flag it if it occurs (date cannot be safely inferred).
# Category: leave missing and flag it if it occurs (category cannot be safely guessed).

for column in ["Age", "Sales"]:
    df[column] = df[column].fillna(df[column].median())

# 6. Remove exact duplicate rows.
df = df.drop_duplicates().copy()

# 7. Detect numeric outliers in Sales using the IQR rule.
q1 = df["Sales"].quantile(0.25)
q3 = df["Sales"].quantile(0.75)
iqr = q3 - q1
lower_limit = q1 - 1.5 * iqr
upper_limit = q3 + 1.5 * iqr

outlier_mask = (df["Sales"] < lower_limit) | (df["Sales"] > upper_limit)
outliers = df.loc[outlier_mask, ["Order_ID", "Sales"]]

print(f"Outliers detected using IQR: {len(outliers)}")
if not outliers.empty:
    print(outliers.to_string(index=False))
print("Outlier decision: Retain detected values for review; do not delete valid sales.")

# 8. Create the after-cleaning statistics.
after_rows = len(df)
after_missing = int(df.isna().sum().sum())
after_duplicates = int(df.duplicated().sum())

summary = pd.DataFrame(
    {
        "Before": [before_rows, before_missing, before_duplicates],
        "After": [after_rows, after_missing, after_duplicates],
    },
    index=["Rows", "Missing Values", "Duplicates"],
)

print("\nBefore / After Cleaning Summary")
print(summary.to_string())

# 9. Save the cleaned data and summary.
df.to_csv(output_file, index=False)
print(f"\nCleaned data saved to: {output_file.name}")
