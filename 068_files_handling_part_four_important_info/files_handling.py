# -------------------------------------
# -- File Handling => Important Info --
# -------------------------------------

import os

# file = open("data.txt", "a")
# # print(file)
# file.truncate(5)
# file.tell()
# print(file.tell())

file = open("data.txt", "r")
file.seek(6)
print(file.read())


# os.remove("path")
