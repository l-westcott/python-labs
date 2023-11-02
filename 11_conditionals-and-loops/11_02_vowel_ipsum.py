# Print the total number of vowels that are used in the lorem ipsum text.

lorem_ipsum = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut 
aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in 
voluptate velit esse cillum dolore eu fugiat nulla pariatur. 
Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt 
mollit anim id est laborum."""

word = ""

for n in lorem_ipsum:
    if n == "a":
        word += n
    elif n == "e":
        word += n
    elif n == "i":
        word += n
    elif n == "o":
        word += n
    elif n == "u":
        word += n
print("The number of vowels in lorem ipsum: ", len(word))