# -------------------
# -- File Handling --
# -------------------
# "a" Append -> Open File For Appending Values, Create File If Not Exists
# "r" Read   -> [Default Value] Open File For Read and Give Error If File is Not Exists
# "w" Write  -> Open File For Writing, Create File If Not Exists
# "x" Create -> Create File, Give Error If File Exists
# --------------------------------------------------

import os

# get the current working directory
cwd = os.getcwd()
print(cwd)
# Directory For The Opened File
absolute_path = os.path.abspath(__file__)
print(absolute_path)
dir_name = os.path.dirname(absolute_path)
print(dir_name)

# Change the Current Working Directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

file = open("data.txt")

# file = open(r"D:\Python\Files\nfiles\osama.txt")
# file = open("D:\Python\Files\osama.txt")

