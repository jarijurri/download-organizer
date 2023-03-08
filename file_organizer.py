import os
import shutil
import configparser
import tkinter as tk
from tkinter import filedialog

# Create the Tkinter app
root = tk.Tk()
root.withdraw()

# Prompt the user to select the directory to organize
download_dir = filedialog.askdirectory(title="Select directory to organized")

# Prompt the user to select the directory where to move organized files
organized_dir = filedialog.askdirectory(title="Select directory where to move organized files")

# Create the config.ini file
config = configparser.ConfigParser()
config['DEFAULT'] = {'download_dir': download_dir, 'organized_dir': organized_dir}
with open('config.ini', 'w') as configfile:
    config.write(configfile)

# Read the configuration file
config = configparser.ConfigParser()
config.read('config.ini')

# Get the download_dir and organized_dir variables from the configuration file
download_dir = config.get('DEFAULT', 'download_dir')
organized_dir = config.get('DEFAULT', 'organized_dir')

# Create a list of all the files in the directory
files = os.listdir(download_dir)

# Create a dictionary to store file types and their corresponding directories
file_types = {}

# Create the organized_dir directory if it doesn't exist
os.makedirs(organized_dir, exist_ok=True)

# Loop through each file in the directory
for file in files:
    # Get the file extension
    file_extension = os.path.splitext(file)[1]
    # If the file extension is not empty
    if file_extension != "":
        # If the file extension is not already in the dictionary, add it
        if file_extension not in file_types:
            file_types[file_extension] = os.path.join(organized_dir, file_extension.strip("."))
            os.makedirs(file_types[file_extension], exist_ok=True)
        # Move the file to the directory corresponding to its file type
        shutil.move(os.path.join(download_dir, file), os.path.join(file_types[file_extension], file))
