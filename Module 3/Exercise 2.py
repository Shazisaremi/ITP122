age = int(input("Enter your age: \n"))
income = int(input("Enter your income: \n"))
if age > 18 and income < 20000:
    print('You are eligible for financial help scheme.')
elif age > 18 and income >20000:
    print('You are not eligible for financial help scheme.')
elif age <18 and income <20000:
    print('You are not eligible for financial help scheme.')
else:
    print('You are not eligible for financial help scheme.')