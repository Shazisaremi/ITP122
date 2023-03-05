gross_income = float(input("Enter your income : "))

gross_income = gross_income - 18500
dependent_num = int(input("number of dependents : "))
gross_income = gross_income - 1200 * dependent_num

flat_tax = 0.25 * gross_income
print("Your tax for this year is equal to : %.3f " %flat_tax)
