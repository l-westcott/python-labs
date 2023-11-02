# Take in a number between 1 and 12 from the user
# and print the name of the associated month:
# "January", "February", ... "December"
# Print "Error" if the number from the user is not between 1 and 12.
# Use a nested `if` statement.

# Request the input from the user

month = input("Please enter a month number (i.e. 1-12): ")
month = int(month)

# If statement to convert & print the number as the month wording

if ((month <= 12) and (month >= 1)) == True:
    if month == 1:
        print("January")
    if month == 2:
        print("February")
    if month == 3:
        print("March")
    if month == 4:
        print("April")
    if month == 5:
        print("May")
    if month == 6:
        print("June")
    if month == 7:
        print("July")
    if month == 8:
        print("August")
    if month == 9:
        print("September")
    if month == 10:
        print("October")
    if month == 11:
        print("Novemer")
    if month == 12:
        print("December")
else:
    print("Error")



