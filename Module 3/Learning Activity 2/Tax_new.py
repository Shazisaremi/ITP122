### Submitted by Zain

# Prompt the user to enter their gross income 
gross_income = float(input("Enter your gross income:"))

# Prompt the user to enter the number of dependents
dependents = int(input("Enter the number of dependents:"))

# Set the standard deduction amount
standard_deduction = 18500

# Set the dependent deduction amount
dependent_deduction = 1200

# Set the tax rate
tax_rage = 0.25

# Calculate the total deductions by adding the standard deduction and dependent deduction * number of dependents
deductions = standard_deduction + dependent_deduction * dependents

# Calculate taxable income by subtracing deductions from gross income. if this value is negative, set it to 0
taxable_income = max(0, gross_income - deductions)

# Calculate income tax by multiplying taxable income by tax rate 
income_tax = taxable_income * tax_rate

# Display calculated income tax
print(f"income tax: {income_tax:.3f}")
