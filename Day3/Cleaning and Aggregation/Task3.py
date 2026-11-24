
import pandas as pd

# Load CSV file
df = pd.read_csv("orders.csv")

# Find missing values and duplicates
print("Missing:", df.isna().sum()["amount"])
print("Duplicates:", df.duplicated().sum())

# Remove duplicates
df = df.drop_duplicates()

# Convert amount to numeric
df["amount"] = pd.to_numeric(df["amount"])

# Find median and fill missing values
median = df["amount"].median()
df["amount"] = df["amount"].fillna(median)
print("Median used:", median)

# Convert order_id to string
df["order_id"] = df["order_id"].astype(str)

# Group by customer_id
result = df.groupby("customer_id").agg(
    total=("amount", "sum"),
    orders=("order_id", "count")
)

print(result)
