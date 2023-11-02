# Ask your user for a number between 0 and 1,000,000,000.
# Use a `while` loop to find the number. When the number is found,
# exit the loop and print the number to the console.

# Request a number from the user

request = input("Please enter a number between 0 & 1,000,000,000 ")
request = int(request)

# While loop to find the number and return it

while request in range(0:1000000000):
    print[request]