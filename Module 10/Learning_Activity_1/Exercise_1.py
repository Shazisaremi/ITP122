def addition(x): # Define the addition function
    if x >= 20: # Do the addition if the x is greater than 20
        return x + addition(x-1) # Sum up the current x with the x - 1
    else:
        return 0 # If x was lower than 20 return 0
result = addition(50)
print("The sum of numbers ranging from 20 to 50 is:", result) # print the result