# Re-create the guess-my-number game from scratch. Don't peek!
# This time, give your players only a certain amount of tries 
# before they lose.

import random
import sys

num = random.randint(1,100)
guess = 0
count = 10

while guess != num:
    guess = input("Please guess a random number between 1 & 100: ")
    guess = int(guess)
    if guess == "quit":
         sys.exit()
    elif guess == num:
        break
    else:
        count -= 1
        if count == 0:
             break
        else:
            print(f"Please try again... You have {count} guesses left")


if count == 0:
     print(f"Sorry you lose, the number was {num}")

if guess == num:
        print("Congratulations you have guessed correctly!")

