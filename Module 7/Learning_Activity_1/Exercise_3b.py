"""
Created on Sat Apr 16 14:28:52 2022

@author: Sheeraz Memon
"""

class Test: # Create a class named Test
    def even_or_odd(self, maxi): # Define a method inside the class name even_or_odd
        for x in range(0,maxi+1): # for numbers from 0 to maxi check the condition below:
            if x%2==0: # if has no remain on division by 2 print is even
                print(x,"is an even number")
            else:
                print(x,"is an odd number")


maxi = int(input("Enter your choice of the value of the end of the range of numbers greater than 0: \n")) #  get the input from user and convert it to integer
obj = Test() # create an object named obj
obj.even_or_odd(maxi) # call the method even_or_odd with the created object