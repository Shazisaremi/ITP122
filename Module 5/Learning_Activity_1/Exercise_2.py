hours = float(input('Enter hours worked: '))
hourlyWage = float(input('Enter dollars paid per hour: '))

if hours <= 40:
    regularHours = hours
    overtime = 0
else:
    overtime = hours - 40
    regularHours = 40

print(hourlyWage*regularHours + (1.5*hourlyWage)*overtime)


