"""
Created on Wed Mar 30 10:56:29 2022

@author: SHEERAZ MEMON
"""
choice = "Y" # Initial Value for choice
valid = ("Y", "y", "n", "N") # Valid choices
yes_list = ("Y", "y", "yes", "Yes", "YES") # Yes valid choices

while choice in yes_list: # only loop on yes valid choices
    weight = float(input("How much do you weight? ")) # Enter the weight
    height = float(input("How tall are you in inches? ")) # Enter the height

    bmi = 703 * (weight / (height * height)) # BMI Calculation
    print("Your BMI is: %.2f" % bmi) # Showing up the BMI

    choice = input("Another BMI calculation (Y/N)? ") # Get the input from user
    while choice not in valid: # While user choices are not in the valid choices set , try again.
        choice = input("Invalid choice.  Enter a Y or N? ") # Enter the valid choice again. 