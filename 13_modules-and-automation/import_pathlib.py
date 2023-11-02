# Import pathlib
import pathlib
# Find the path to my Desktop
path = pathlib.Path("/Users/lrwes/OneDrive/Desktop")

# Create a new folder
new_path = pathlib.Path("/Users/lrwes/OneDrive/Desktop/Screenshots")
new_path.mkdir(exist_ok=True)

# List all the files on there
# Filter for screenshots only
for filepath in path.iterdir():
    if filepath.suffix == ".png":
        # Create new path for each file
        new_filepath = new_path.joinpath(filepath.name)
        # Move the screenshots in there
        filepath.replace(new_filepath)


