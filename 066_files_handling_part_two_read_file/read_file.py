# --------------------------------
# -- File Handling => Read File --
# --------------------------------

# import os

# absolute_path = os.path.abspath(__file__)
# print(absolute_path)

# file = open("data.txt", "r")
file = open("/Users/naserebedo/Developer/python/python/066_files_handling_part_two_read_file/data.txt", "r")

# print('\n')
# print(file)             # -> file data object
# print(file.name)
# print(file.mode)
# print(file.encoding)
# print('\n')

# print(file.read())      # default -1 means all
# print(file.read(5))
# print(file.readline())
# print(file.readline(10))

# print(file.readlines())
# print(type(file.readlines()))

for line in file:
    print(line)
    if line.startswith('I am a'):
        break


# close the file
file.close()
