import random

start = 1
end = 100
num = random.randint(start, end)
guess = None
count = 10

while (guess != num) and (count > 0) == True:
    guess = input(f"Please guess a number between {start} and {end}: ").lower()
    if guess == "exit":
        print("Goodbye")
        break
    guess = int(guess)
    if guess == num:
        print("Congratulations!")
    else:
        count -= 1
        if count == 0:
            print("Sorry you have run out of chances")
            break
        else:
            print("sorry try again")