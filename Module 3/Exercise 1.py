user_input = input('Enter a temp value in either Celsius or Fahrenheit as 22C or 70F: \n')
degree = float(user_input[:-1])
F_or_C = user_input[-1]
Tf = (degree*((9/5)+32))
Tc = ((degree-32)*5/9)
if F_or_C.upper() == "C":
    output = Tf
    F_or_C = "Fahrenheit"

elif F_or_C.upper() == "F":
    output = Tc
    F_or_C = "Celsius"

else:
    print("\nError: Add suffix C or F to your temparature reading to indicate whether the temparature is in Celsius or Farenheit!")

print("\nThe temperature is: %.4f" %output, F_or_C)