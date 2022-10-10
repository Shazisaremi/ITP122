number = input("Enter an integer: ")
try:
    number=int(number)
    if number%5==0:
        print(number, "is a multile of 5")
    else:
        print(number, "is not a multiple of 5")
except:
    print("Please enter a number")