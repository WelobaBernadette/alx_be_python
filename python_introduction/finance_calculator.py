income = float(input("Enter your monthly income: "))
expenses = float(input("Enter your total monthly expenses: "))

monthly_savings = income - expenses

Projected Savings = Monthly Savings * 12 + (Monthly Savings * 12 * 0.05)

print("Your monthly savings are ${monthly_savings}.")
print("Projected savings after one year, with interest, is: ${projected_savings}.")
