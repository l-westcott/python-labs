# What data type is the variable `mystery` at the end of the script?
# What data types does it hold at certain points earlier in the script?

mystery = None
print("After the 1st variable set, the variable type is ", type(mystery))
mystery = "Sommerfeld"
print("After the 2nd variable set, the variable type is ", type(mystery))
mystery = 137
print("After the 3rd variable set, the variable type is ", type(mystery))
mystery = mystery + 0.0
print("At the end of the script, the variable type is ", type(mystery))