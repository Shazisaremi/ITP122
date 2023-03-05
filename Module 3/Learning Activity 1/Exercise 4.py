import re # Import Regex Library
user_input = input("Enter your password: \n") # Get the user's password
temp = True # A flag to check if the password entered is true. 
while temp: # While True
    if (len(user_input)<5 or len(user_input)>20): # Check the length of password to be in range 5 - 20 Characters
        break
    elif not re.search("[A-Z]",user_input): # Check if the higher letters is exists in the password
        break
    elif not re.search("[a-z]",user_input): # Check if the lower letters is exists in the password
        break
    elif not re.search("[0-9]",user_input): # Check if the numbers is exists in the password
        break
    elif not re.search("[$#@]",user_input): # Check if the Special characters is exists in the password
        break
    elif re.search("\s",user_input):  # Check if space not exitst in the password
        break
    else:
        print("\nValid Password") # if all the conditions are passed, then shows the user Valid Password
        temp = False
        break
if temp:
    print("\nNot a Valid Password") # Else not.
