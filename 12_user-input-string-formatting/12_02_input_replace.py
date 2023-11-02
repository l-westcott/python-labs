# Write a script that takes a string of words and a symbol from the user.
# Replace all occurrences of the first letter with the symbol. For example:
#
# String input: more python programming please
# Symbol input: §
# Result: §ore python progra§§ing please

# Request variable inputs
string = input("Type a phrase: ")
symbol = input("Type a symbol: ")
string_2 = ""

# find and replace the first letter and it's occurences with the symbol
for n in string:
    if n == string[0]:
        string_2 += symbol
    else:
        string_2 += n

# print the answer
print("Your phrase where the first letter and all it's occurences converted: ", string_2)