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

source_folder = "module-2-python-basics/file-sorting"
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
One mistake I experienced was using a folder path that does not exist. Turns out, the source folder name is wrong, making it so that the program will not be able to find the files.


============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================
This connects to automation because the computer can repeat the same file-organizing task without me manually moving every file.
In the future, as a secretary right now, I could use a similar idea for schoolwork documents and files by automatically organizing assignments, PDFs, screenshots, or other files into different folders.
"""