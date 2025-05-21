income = input("Enter your monthly income:")
expense = input("Enter your monthly expenses:")
monthly_savings = int(income) - int(expense);
project_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)
print(f"Your monthly savings are ${monthly_savings}")
print(f"Projected savings after one year, with interest, is: ${project_savings}")