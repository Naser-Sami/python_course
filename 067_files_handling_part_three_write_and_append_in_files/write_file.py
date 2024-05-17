# -----------------------------------------------
# -- File Handling => Write and Append In File --
# -----------------------------------------------

path = "/Users/naserebedo/Developer/python/python/067_files_handling_part_three_write_and_append_in_files/"

# file = open(f"{path}data.txt", "r") # read
file = open(f"{path}data.txt", "w")   # write
file.write("Hello, World!\n")
file.write("Second line\n")

_list_ = ["Today is a perfect day.\n", "I'm the hero.\n", "I know what I do!\n", "Welcome to my club!\n"]
file.writelines(_list_)

file = open(f"{path}data.txt", "a")   # append
# file.write("Hello Mee!")
file.write("\n\n\nWelcome Back!\n\n\n")
