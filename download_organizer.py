import os
import shutil

# Define the directory path
path = "C:/Users/user/Downloads"

# Create a list of all the files in the directory
files = os.listdir(path)

# Create a dictionary to store file types and their corresponding directories
file_types = {}

# Create a folder called "organized_downloads" in the "D:" drive
organized_path = "D:/organized_downloads"
os.makedirs(organized_path, exist_ok=True)

# Loop through each file in the directory
for file in files:
    # Get the file extension
    file_extension = os.path.splitext(file)[1]
    # If the file extension is not empty
    if file_extension != "":
        # If the file extension is not already in the dictionary, add it
        if file_extension not in file_types:
            file_types[file_extension] = os.path.join(organized_path, file_extension.strip("."))
            os.makedirs(file_types[file_extension], exist_ok=True)
        # Move the file to the directory corresponding to its file type
        shutil.move(os.path.join(path, file), os.path.join(file_types[file_extension], file))
