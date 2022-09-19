twoway_ticket = 400
extra_charge = (15/100) * twoway_ticket
upgraded_price = extra_charge + twoway_ticket
discount = (20/100) * upgraded_price
final_price = upgraded_price - discount
print("The total amount Alice has to pay is: $%.2f" %final_price)