import random
random_number = random.randint(50, 100) # generates a random number between 50 to 100
count=0 # The user has 5 chances to guess it correctly after which the game is over
while count<=5: # The user has 5 chances to guess it correctly after which the game is over
    guess = int(input("Enter your guess: \n"))
    count+=1
    if guess == random_number: # If the user’s guess is equal to the random number generated and the user has guessed the number within his 5 chances, the user has won.
        print("\nYour guess is correct!\n")
        break
    elif guess < random_number:
        print("Your guess is lower than the correct answer!")
    elif guess > random_number:
        print("Your guess is higher than the correct answer!")
else: # If the user gets all his 5 guesses wrong, then the user has lost.
    print("You have run out of guesses! Try again :)")