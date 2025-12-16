# 1. User Input for Financial Details
# Use float() instead of int() to allow for decimal amounts (e.g., 2500.50)
income = float(input("Enter your monthly income: "))
expenses = float(input("Enter your total monthly expenses: "))

# 2. Calculate Monthly Savings
monthly_savings = income - expenses

# 3. Project Annual Savings (using the specified formula)
# Formula: Projected Savings = Monthly Savings * 12 + (Monthly Savings * 12 * 0.05)
annual_savings_base = monthly_savings * 12
interest_rate = 0.05  # 5% annual interest rate

# Calculation of projected savings using the required formula
projected_savings = annual_savings_base + (annual_savings_base * interest_rate)

# 4. Output Results
# We use an f-string and round the numbers to 2 decimal places for currency format
print(f"\nYour monthly savings are ${monthly_savings:.2f}.")
print(f"Projected savings after one year, with interest, is: ${projected_savings:.2f}.")