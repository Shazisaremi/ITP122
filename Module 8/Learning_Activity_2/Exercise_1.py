"""
Created on Wed Mar  9 14:09:00 2022

@author: SHEERAZ MEMON
"""

print("------------------------------")
print("\t Welcome to Torrens Cafe")
print("-"*30)

print("1. Small brekky $10")
print("4. egg ($0.99)")
print("5. toast ($0.79)")



print('\n\n\n<Enter 000 to exit and 111 to finalize the payment>')


total=0
while True:
    itemChoice=input("Choose your item: ")
    if int(itemChoice)==1:#or ---->      if itemChoice=="1":
        quant=int(input("Quantity: "))
        total=total+10*quant
    elif int(itemChoice)==4:
        quant=int(input("Quantity: "))
        total=total+0.99*quant
    elif int(itemChoice)==5:
        quant=int(input("Quantity: "))
        total=total+0.79*quant
    elif (itemChoice)=='000':#quit
        break
    elif itemChoice=='111':#finalize payment
        print("Total: {}".format(total))
        break
    else:
        print('# Item Not Found, Try Again.')