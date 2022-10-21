#Compute a person’s salary.Significant constants are regular-hours price, after-hours price , total hours
# The inputs are regular hours and after-hours working time


#The outputs are the income tax
TOTAL_SALARY = 5000
TOTAL_HOURS = 100
AFTER_HOURS_PRICE = 25

# Request the inputs

TOTAL_REGULAR_HOURS_WORK = int(input("Enter the regular-hours : "))
TOTAL_AFTER_HOURS_WORK = int(input("Enter the after-hours : "))

# Compute the salary

if TOTAL_REGULAR_HOURS_WORK >= TOTAL_HOURS:
    SALARY = TOTAL_SALARY
else:
    SALARY = TOTAL_SALARY * (TOTAL_REGULAR_HOURS_WORK/TOTAL_HOURS)

if TOTAL_AFTER_HOURS_WORK > 0:
    SALARY += TOTAL_AFTER_HOURS_WORK * AFTER_HOURS_PRICE

# Display the salary

print("The salary is $" + str(SALARY))

