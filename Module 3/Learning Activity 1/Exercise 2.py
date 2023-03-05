age = int(input("Enter your age: \n")) # Get the user's age and convert it to integer then store it to age variable.
income = int(input("Enter your income: \n")) # Get the user's income and convert it to intetger then store it to age variable.
if age > 18 and income < 20000: # Check the condition 
    print('You are eligible for financial help scheme.')
elif age > 18 and income >20000: # Check the condition 
    print('You are not eligible for financial help scheme.')
elif age <18 and income <20000: # Check the condition
    print('You are not eligible for financial help scheme.')
else: # Else none of conditions above were true, then do: 
    print('You are not eligible for financial help scheme.')
