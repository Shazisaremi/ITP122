maxi = int(input("Enter your choice of the value of the end of the range of numbers greater than 0: \n")) # get the input from user and convert it to integer
def even_or_odd(maxi): # Define the even_or_odd function with number as input
    for x in range(0,maxi+1): # for numbers from 0 to maxi check the condition below:
        if x%2==0: # if has no remain on division by 2 print is even
            print(x,"is an even number")
        else:
            print(x,"is an odd number")

even_or_odd(maxi) # Call the function