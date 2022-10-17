#Compute a person’s income tax. Significant constants are tax rate, standard deduction, and
#deduction per dependent
# The inputs are gross income and number of dependents
# Computations:
# taxable income = gross income - the standard deduction - a deduction for each dependent
#income tax = is a fixed percentage of the taxable income

#The outputs are the income tax

TAX_RATE = 0.20
STANDARD_DEDUCTION = 10000.0
DEPENDENT_DEDUCTION = 3000.0

# Request the inputs

grossIncome = float(input("Enter the gross income: "))
numDependents = int(input("Enter the number of dependents: "))

# Compute the income tax

taxableIncome =grossIncome-STANDARD_DEDUCTION-(DEPENDENT_DEDUCTION * numDependents)
incomeTax = taxableIncome * TAX_RATE

# Display the income tax

print("The income tax is $" + str(incomeTax))