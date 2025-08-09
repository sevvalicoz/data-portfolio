import pandas as pd
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv("sales.csv", parse_dates=["date"])

# Calculate revenue
df["revenue"] = df["units"] * df["unit_price"]

# KPIs
total_rev = df["revenue"].sum()
top_product = df.groupby("product")["revenue"].sum().sort_values(ascending=False).index[0]
top_region = df.groupby("region")["revenue"].sum().sort_values(ascending=False).index[0]

print("Total Revenue:", total_rev)
print("Top Product by Revenue:", top_product)
print("Top Region by Revenue:", top_region)

# Daily revenue chart
daily = df.groupby("date")["revenue"].sum()
ax = daily.plot(title="Daily Revenue", marker='o')
ax.set_xlabel("Date")
ax.set_ylabel("Revenue")
plt.tight_layout()
plt.savefig("daily_revenue.png")
