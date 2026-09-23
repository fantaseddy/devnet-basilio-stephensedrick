"""
Module 2 — Activity: File Sorting with os and shutil
Student: Stephen Sedrick C. Basilio
Date: September 23, 2026

============================================
WHAT DID YOU BUILD? (explain in your own words)
============================================
This is similar to the previous activity that our professor assigned to us in the lab before. I built a simple file-sorting script using Python's os and shutil modules. The script checks the files inside a folder and sorts them into different folders based on their file extension. For example, image files such as .jpg and .png are placed in an Images folder, while .txt and .docx files can be placed in a Documents folder. The rule I used to sort the files is their file extension. This makes it easier to organize files automatically instead of moving each file manually.


============================================
KEY VOCABULARY
============================================
- os module: Python module that lets a program work with the operating system, such as checking folders and file names
- shutil module: Python module used for high-level file operations, including moving and copying files
- file path: location of a file or folder in the computer
- directory: folder where files and other folders are stored
(add more as needed)
- file sorting: checks files and sorts them into different folders based on their file extension
- file extension: the part of a file name that usually shows what type of file it is, such as .txt, .jpg, or .pdf
- automation: using a program to perform a task automatically instead of doing it manually


============================================
YOUR SCRIPT
============================================
Paste the code you already wrote for this activity below.
"""

import os
import shutil

source_folder = "files"
folders = { ".jpg": "Images", ".png": "Images", ".txt": "Documents", ".pdf": "Documents", ".docx": "Documents" }

for filename in os.listdir(source_folder):
    file_path = os.path.join(source_folder, filename)
    if os.path.isfile(file_path):
        extension = os.path.splitext(filename)[1].lower()
        if extension in folders:
            destination_folder = os.path.join(source_folder, folders[extension])
            os.makedirs(destination_folder, exist_ok=True)
            shutil.move(file_path, os.path.join(destination_folder, filename))

print("Files have been sorted.")


"""
============================================
A MISTAKE I MADE (or one I want to avoid)
============================================
[what tripped you up while building this? e.g. a path that didn't
exist, a file that got overwritten, something that didn't work the
way you expected at first]


============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================
[optional: how is this similar to what real automation scripts do?
think about your own gradebook/attendance workflow — could something
like this save you time there?]
"""
