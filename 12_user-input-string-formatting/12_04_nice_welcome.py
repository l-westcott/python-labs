# Ask the user to input their name. Then print a nice welcome message
# that welcomes them personally to your script.
# If a user enters more than one name, e.g. "firstname lastname",
# then use only their first name to overstep some personal boundaries
# in your welcome message.

# Ask User for their name
name = input("Please type your name: ")
first_name = ""

# find the index of the space
if " " in name:
    space = name.find(" ")
    print(f"Welcome {name[0:space]} to the world")
else:
    print(f"Welcome {name} to the world")
