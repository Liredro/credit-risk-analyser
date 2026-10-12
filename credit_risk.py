import pandas as pd
import matplotlib.pyplot as plt

# 1. Load loan data
df = pd.read_csv("loans.csv")

# 2. Calculate portfolio statistics
total_loans = len(df)
total_balance = df["balance"].sum()
total_defaults = df["defaulted"].sum()

default_rate = (total_defaults / total_loans) * 100

overdue_loans = (df["days_past_due"] >= 30).sum()
overdue_rate = (overdue_loans / total_loans) * 100

# 3. Display portfolio summary
print("=== LOAN PORTFOLIO ANALYSIS ===")

print(f"Total loans: {total_loans}")
print(f"Outstanding balance: £{total_balance:,.2f}")
print(f"Defaults: {total_defaults}")
print(f"Default rate: {default_rate:.2f}%")
print(f"30+ day overdue rate: {overdue_rate:.2f}%")

# 4. Compare loan types
risk_by_type = df.groupby("loan_type")["defaulted"].mean() * 100

print("\n=== DEFAULT RATE BY LOAN TYPE ===")
print(risk_by_type.round(2))

# 5. Create and save a chart
risk_by_type.plot(kind="bar")

plt.title("Default Rate by Loan Type")
plt.ylabel("Default Rate (%)")
plt.xlabel("Loan Type")
plt.tight_layout()

plt.savefig("default_rates.png")
print("\nChart saved as default_rates.png")
