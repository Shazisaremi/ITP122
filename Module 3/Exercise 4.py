import re
user_input = input("Enter your password: \n")
temp = True
while temp:
    if (len(user_input)<5 or len(user_input)>20):
        break
    elif not re.search("[A-Z]",user_input):
        break
    elif not re.search("[a-z]",user_input):
        break
    elif not re.search("[0-9]",user_input):
        break
    elif not re.search("[$#@]",user_input):
        break
    elif re.search("\s",user_input):
        break
    else:
        print("\nValid Password")
        temp = False
        break
if temp:
    print("\nNot a Valid Password")