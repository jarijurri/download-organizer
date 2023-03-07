# File-organizer

File-organizer is designed to organize files in a directory by grouping them into subdirectories based on their file types.

File-organizer uses the os, shutil, configparser, and tkinter modules. The tkinter module is used to create a graphical user interface (GUI) that prompts the user to select a directory to organize and a directory to move the organized files to.

File-organizer then creates a config.ini file to store the selected directories using the configparser module and reads the selected directories from the config.ini file.

Next, the File-organizer gets a list of all the files in the selected download directory using the os.listdir() function. It then creates an empty dictionary to store file types and their corresponding directories.

File-organizer loops through each file in the download directory and gets its file extension using the os.path.splitext() function. If the file extension is not empty and not already in the file_types dictionary, it adds the file extension and its corresponding directory to the file_types dictionary and creates the corresponding subdirectory in the selected organized directory using the os.makedirs() function with the exist_ok=True option.

Finally, the File-organizer moves each file to the directory corresponding to its file type using the shutil.move() function. This way, the script organizes all the files in the selected download directory into subdirectories based on their file types in the selected organized directory.


# Clone the repository
git clone https://github.com/jarijurrie/file-organizer.git

# Navigate to the directory where you have stored the script in the command line
cd your_repository

# Install the necessary dependencies using pip
pip install -r requirements.txt

# Run the script
python file_organizer.py
