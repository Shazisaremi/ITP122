user_input = input('Enter a temp value in either Celsius or Fahrenheit as 22C or 70F: \n') # get the input temperature from user in the following format %d[C-F]
degree = float(user_input[:-1]) # Convert the charachters before the last symbol to float type
F_or_C = user_input[-1] # Store the symbol in another variable
Tf = (degree*((9/5)+32)) # The formula to convert clesius to Farenhait 
Tc = ((degree-32)*5/9) # The formula for conversion of farenhait to clesius
if F_or_C.upper() == "C": # Check if the symbol is C
    output = Tf # Store the Farenhait Conversion result to output
    F_or_C = "Fahrenheit" 

elif F_or_C.upper() == "F": # Check if the symbol is F
    output = Tc # store the Clesius Conversion Result to output
    F_or_C = "Celsius"

else: # Else the input is wrong, print the error message.
    print("\nError: Add suffix C or F to your temparature reading to indicate whether the temparature is in Celsius or Farenheit!")

 # Print the result 
print("\nThe temperature is: %.4f" %output, F_or_C)
