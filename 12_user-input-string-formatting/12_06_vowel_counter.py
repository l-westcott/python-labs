# Write a script that takes a string input from a user
# and prints a total count of how often each individual vowel appeared.

# Request a string from the user

string = input("Please enter a random word or phrase: ")
string = string.lower()

# Count how many of each vowels appear

av = ""

for a in string:
    if a == "a":
        av += a

print("The number of a's in your word / phrase: ", len(av))

ev = ""

for e in string:
    if e == "e":
        ev += e

print("The number of e's in your word / phrase: ", len(ev))

iv = ""

for i in string:
    if i == "i":
        iv += i

print("The number of i's in your word / phrase: ", len(iv))

ov = ""

for o in string:
    if o == "o":
        ov += o

print("The number of o's in your word / phrase: ", len(ov))

uv = ""

for u in string:
    if u == "u":
        uv += u

print("The number of u's in your word / phrase: ", len(uv))