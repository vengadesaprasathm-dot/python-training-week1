
import pandas as pd
import matplotlib.pyplot as plt

# Read employees CSV
df = pd.read_csv("employees.csv")

# 1. Bar Chart - Average Salary by Department
avg_salary = df.groupby("department")["salary"].mean()

plt.bar(avg_salary.index, avg_salary.values)
plt.title("Average Salary by Department")
plt.xlabel("Department")
plt.ylabel("Average Salary")

for i, value in enumerate(avg_salary.values):
    plt.text(i, value, str(int(value)), ha="center", va="bottom")

plt.tight_layout()
plt.savefig("bar_chart.png")
plt.show()


# 2. Histogram - Salary Distribution
plt.hist(df["salary"], bins=5, edgecolor="black")
plt.title("Salary Distribution")
plt.xlabel("Salary")
plt.ylabel("Frequency")

plt.tight_layout()
plt.savefig("histogram.png")
plt.show()


# 3. Scatter Plot - ID vs Salary by Department
for dept in df["department"].unique():
    data = df[df["department"] == dept]
    plt.scatter(data["id"], data["salary"], label=dept)

plt.title("Employee ID vs Salary")
plt.xlabel("Employee ID")
plt.ylabel("Salary")
plt.legend()

plt.tight_layout()
plt.savefig("scatter_plot.png")
plt.show()


# 4. Line Chart - Monthly Sales
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sales = [12, 15, 14, 18, 22, 25]

plt.plot(months, sales, marker="o")
plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.tight_layout()
plt.savefig("line_chart.png")
plt.show()
