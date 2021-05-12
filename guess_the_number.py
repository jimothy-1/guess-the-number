import random

number = random.randint(0, 100)

while True:
    user_guess = int(input("Enter in your guess: "))
    if user_guess > number:
        print("Lower")
    elif user_guess < number:
        print("Higher")
    else:
        print("You won! The number was " + str(number))
        break
    