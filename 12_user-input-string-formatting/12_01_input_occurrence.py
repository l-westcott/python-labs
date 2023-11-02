# Write a script that takes a string of words and a letter from the user.
# Find the index of first occurrence of the letter in the string. For example:
#
# String input: hello world
# Letter input: o
# Result: 4

# Input variable questions
string = input("Type a phrase: ")
letter = input("Type a letter: ")

# Finding the result
result = string.find(letter)

# Display the outcome
print("The index of the first occurence of the letter within your phase is: ", result)