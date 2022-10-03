investment_amount = float(input("Enter the investment amount:\t"))

num_year = int(input("Enter the number of years(as 1 or 2 or 3 or... or 10):\t"))

rate = float(input("Enter the rate as (Ex: 0, 1.5, 5.9, 8 etc)%:\t"))

starting_balance = investment_amount
total_interest = 0
print("Year\tStarting Balance\tInterest\tEnding Balance")
for year in range(1, num_year + 1):
    interest =  starting_balance * rate / 100
    ending_balance = starting_balance + interest
    print("{}\t{:.1f}\t{:.1f}\t{:.1f}".format(year, starting_balance, interest, ending_balance))
    starting_balance = ending_balance
    total_interest += interest


print("Ending Balance: \t {:.3f}".format(ending_balance))
print("Total Interest Earned: \t {:.3f}".format(total_interest))