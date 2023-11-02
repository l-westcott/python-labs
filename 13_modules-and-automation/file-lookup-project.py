# Import pathlib module

import pathlib

# Define variable

python = ""
png = ""

# Define lookup path

path = pathlib.Path("/Users/lrwes/OneDrive/Documents/codingnomads/python-101-main/projects")

# For loop to pick out each file

for filepath in path.iterdir():
    if filepath.suffix == ".py":
        python += str(filepath) + " "
    if filepath.suffix == ".png":
        png += str(filepath) + " "

# list each file in 
print("The List of python files: ", python)
print("The list of jpg files: ", png)