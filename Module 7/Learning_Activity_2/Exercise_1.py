# Part A

shopping_list = ['bread', 'rice', 'chocolates', 'cooking oil', 'sugar', 'salt', 'milk', 'chocolates', 'noodles',
                 'bread', 'cheese', 'laundry powder', 'bread', 'chips', 'chocolates', 'cooking oil', 'frozen peas',
                 'ice cream', 'cookies', 'noodles', 'tomatoes', 'onions', 'garlic', 'capsicum', 'spinach', 'pasta',
                 'laundry powder', 'orange juice', 'apples', 'oats', 'cookies']

def no_of_times_repeated(shopping, product):
    count = 0
    for item in shopping:
        if item == product:
            count += 1
    print(f"There is {count} {product} in the shopping list")

no_of_times_repeated(shopping_list, 'cookies')

# Part B

def rem_rep(shopping):
    list_to_set = set(shopping) # Set items are unique so, the duplicated items will be removed
    set_to_list = list(list_to_set) # Convert the set to list
    return set_to_list # Return the list of shopping without duplication

shopping_list = rem_rep(shopping_list)
print(shopping_list)
