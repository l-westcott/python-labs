# Ask for the player's name
name = input("What is your name: ")
# Hard-code a word that needs to be guessed in the script
import random
words = ("hello", "chicken", "poo", "weep", "running", "porridge", "pig", "hamster", "titties")
word = word_nochange = random.choice(words)
# Print an explanation to the user
count = 10
print(f"This is a game of hangman, you have {count} tries to guess the word")
# Display the word as a sequence of blanks, e.g. "_ _ _ _ _" for "hello"
guess_full = len(word) * "_"
print("This word to guess is: ", guess_full)
# Ask for user input
guess = None

while (word != len(word)*" ") and (count != 0) == True:
    guess = input("Please enter a single digit: ").lower()
    if (len(guess) > 1) or (guess == "") or (guess == " ")== True : # Allow only single-character alphabetic input
        print("Please only input a single character...")
        continue
    else:
        if (guess in word) == True: # If letter is correct, add to the word
            guess_full = guess_full[:word.find(guess)] + guess + guess_full[word.find(guess)+1:]
            word = word[:word.find(guess)] + " " + word[word.find(guess)+1:]
            print(f"CORRECT!!! You have {count} tries remaining & the word looks like {guess_full}")
            continue
        if (guess in guess_full) == True: # filter out the guesses already tried
            print("You have already guessed that... try again...")
        else: # Display an incorrect message and reduce the count
            count -= 1
            print(f"INCORRECT!!! You have {count} tries remaining & the word looks like {guess_full}")
            continue

if (count == 0) == True:
    print(f"Sorry {name}, you lose! The word was {word_nochange}")
else:
    print(f"Congratulations {name}, you win!")