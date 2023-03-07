# download-organizer
This Python script reads the files in the default Windows download folder and creates a new directory for each file extension it finds. It first creates an empty dictionary to store the file extensions and their corresponding directories. Then it loops through each file in the default Windows download folder, gets its file extension, and checks if the file extension is not empty. If the file extension is not empty, it checks if the file extension is already in the dictionary. If it is not, it creates a new directory with the same name as the file extension in the "organized_path" directory specified by the user. Finally, it moves the file to the directory corresponding to its file extension.

Instructions:

-1. Replace the "organized_path" variable with the directory path where you want to create the new directories for each file extension. By default, the variable is set to 
"D:/organized_downloads", but you can change it to any directory path you like.

2. Run the Python script. It will read the files in the default Windows download folder and create a new directory for each file extension it finds in the "organized_path" 
directory you specified in step 1. The script will move the corresponding files to the new directories.

3. If you want to change the directory path after running the script, you can simply modify the "organized_path" variable in the script and run it again.
