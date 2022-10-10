first = 0
second = 1
print(first, second, end=" ")

while first < 50:

    #Printing the next Fibonacci number.
    print(first + second, end=" ")

    #Updating the first and second variables for finding the next number.
    temp = second
    second = first + second
    first = temp
