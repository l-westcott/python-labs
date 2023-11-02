# Write a program that takes a number between 1 and 1,000,000,000
# from the user and determines whether it is divisible by 3 using an `if` statement.
# Print the result.

# Request a number
num = input("Type a number between 1 and 1,000,000,000: ")

# If statement to determine if it is divisble by 3

if (int(num) % 3) == 0:
    print("Your number is divisible by 3!")
else:
    print("Your number is NOT divisible by 3!")
