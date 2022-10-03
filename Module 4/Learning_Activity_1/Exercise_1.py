user_input = input("Enter values of your choice separated by commas ") # Take the input like the following format from user:
# user_input = 9, 10, 11, 5, 6
print(user_input)

temp1 = user_input.split(",") # To eliminate commas, split() returns list of seperated items by , .
conv_list = list(temp1) # Its not necessary to convert list to list
print(conv_list) # Print the list of items

temp2 = user_input.split(",") # To eliminate commas, split() returns list of seperated items by , .
conv_tuple = tuple(temp2) # Convert list of items to tuple
print(conv_tuple) # Print the tuples.