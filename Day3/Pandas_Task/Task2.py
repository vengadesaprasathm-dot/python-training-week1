
import pandas as pd

# Load CSV file
df = pd.read_csv("employees.csv")

# Display basic information
print(df.head())
df.info()
print(df.describe())

# Select columns
print(df["name"])
print(df[["name", "salary"]])

# Chennai employees using loc
print("Chennai:", ", ".join(df.loc[df["city"] == "Chennai", "name"]))

# Slice using iloc
print(df.iloc[0:3, 1:3])

# Filter salary above 50000
high_salary = df[df["salary"] > 50000]
print("Salary above 50000:", len(high_salary), "employees")

# Filter IT employees
it_employees = df[df["department"] == "IT"]
print("IT department:", ", ".join(it_employees["name"]))
