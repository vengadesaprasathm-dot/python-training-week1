
import pandas as pd

# Load CSV files
orders = pd.read_csv("orders.csv")
customers = pd.read_csv("customers.csv")

# Inner join
inner = pd.merge(orders, customers, on="customer_id", how="inner")
print("Inner join rows:", len(inner))
print(inner)

# Left join
left = pd.merge(customers, orders, on="customer_id", how="left")
print("No orders:", left[left["order_id"].isna()]["name"].tolist())

# Outer join
outer = pd.merge(orders, customers, on="customer_id", how="outer", indicator=True)
print("Order without customer:")
print(outer[outer["_merge"] == "left_only"][["customer_id"]])

