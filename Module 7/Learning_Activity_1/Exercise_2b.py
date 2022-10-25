"""
Created on Sat Apr 16 14:37:20 2022

@author: Sheeraz Memon
"""
class Palindrome: # Define the Palindrome Class
    def check_palindrome(self,userInput): # Define a method inside the palindrome class
        reverse=userInput[::-1] # Reverse the input string
        if userInput==reverse: # Check if the string is equal to reversed string
            print('The string you entered is a palindrome')
        else:
            print('The string you entered is NOT a palindrome')



userInput=input('Enter the string you want to check:')
obj = Palindrome() # Create a object with type of Palindrome class
obj.check_palindrome(userInput) # Call the check_palindrome method with the created object.