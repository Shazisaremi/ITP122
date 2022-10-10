age = int(input("Enter your age:\t"))
len_of_citizen = int(input("US citizen for how many years ?\t"))

if age >= 30 and len_of_citizen >= 9:
    print("You are eligible to be senator...")
else:
    print("You are not eligible to be senator...")