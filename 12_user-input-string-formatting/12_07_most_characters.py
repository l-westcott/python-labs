# Write a script that takes three strings from the user
# and prints the longest string together with its length.
#
# Example Input:
#     hello
#     world
#     greetings
#
# Example Output:
#     9, greetings

# Request for the 3 inputs:

input_1 = input("Please enter your 1st input: ")
input_2 = input("Please enter your 2nd input: ")
input_3 = input("Please enter your 3rd input: ")

# Find the longest input

if ((len(input_1) > (len(input_2))) and ((len(input_1) > len(input_3)))) == True:
    print(len(input_1), ", ", input_1)

if ((len(input_2) > (len(input_1))) and ((len(input_2) > len(input_3)))) == True:
    print(len(input_2), ", ", input_2)    

if ((len(input_3) > (len(input_1))) and ((len(input_3) > len(input_1)))) == True:
    print(len(input_3), ", ", input_3)    