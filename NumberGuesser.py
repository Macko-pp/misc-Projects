# Imports-----------------------------------------------------------------------

import random
import sys

# Input-And-Score----------------------------------------------------------------

print("Number Guesser!")

score = 50

while True:
    print("Current Score", score)

    if score <= 0:
        print("Your score reached zero! You loose! :(")
        sys.exit()

    guess = input("Guess a Number (1-10): ")

    if guess == "end":
        sys.exit()

    else:
        try:
            guess = int(guess)
        except:
            print("\nPlease input a whole number\n")
            continue

    # Innerworkings-------------------------------------------------------------

    if guess != ans:
        print("\nNo… That's not it…\n")
        score = score - 5

    elif guess == ans:
        ans = random.randint(1, 10)

        print("\nYay! You Guessed it!\n")
        score = score + 10
