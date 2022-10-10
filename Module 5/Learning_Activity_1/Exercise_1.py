unit_cost = 100
quantity = int(input("Enter the number of items"))

price = quantity * unit_cost
if price > 1000:
    price = price - price/10

print("Total Cost:\t", price)