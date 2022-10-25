"""
Created on Thu Mar 31 20:02:43 2022

@author: SHEERAZ MEMON
"""

def palindrome(userInput): # Define the palindrome function with userInput as input
    reverse=userInput[::-1] # Reverse the input string
    if userInput==reverse: # Check if the string is equal to reversed string
        print('The string you entered is a palindrome')
    else:
        print('The string you entered is NOT a palindrome')

def main(): # Use main function to run the code
    userInput=input('Enter the string you want to check:') # Get the input string from user
    palindrome(userInput) # Call the function.

main()