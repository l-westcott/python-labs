# Use a `for` loop to print out every fifth number counting from 1 to 1000.
# i.e. sum 5, 10, 15, 20 ...

fifth = ""

for n in range(5,1001,5):
    fifth += str(n) + " "
print(fifth)
    