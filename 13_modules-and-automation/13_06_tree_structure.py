# Write a script that walks through a nested folder structure 
# and prints out all the Python files it can find.
# Run it in your labs folder and add formatting for nicer viewing.

import pathlib

path = pathlib.Path("/Users/lrwes/OneDrive/Documents/codingnomads\python-101-main\projects")

for filepath in path.iterdir():
    if filepath.suffix == ".py":
        print(filepath.name)
    else:
        print("Not a python file")