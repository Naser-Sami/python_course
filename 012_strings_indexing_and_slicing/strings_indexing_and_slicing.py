# ---------------------------------
# Strings Indexing & Slicing
# [1] All Data in Python is Object
# [2] Object Contain Elements
# [3] Every Element Has Its Own Index
# [4] Python Uses Zero-Based Indexing (Index Start From Zero)
# [5] Use Square Brackets To Access Element
# [6] Enable Accessing Parts Of Strings, Tuples or Lists
# ---------------------------------

# Indexing (Access Single Item)
i_love_python = "I Love Python"
print(i_love_python)
print(i_love_python[9])
print(i_love_python[-3])


# Slicing (Access Multiple Sequence Items)
# [Start:End] End Not Included* [ start 1 : end (n - 1) ]
# [Start:End:Steps]

print(i_love_python[8:11])          # yth
print(i_love_python[3:5])           # ov

print(i_love_python[:10])           # If Start Is Not Here Will Start From 0 (I Love Pyt)
print(i_love_python[5:])            # If End Is Not Here Will Go To The End (e Python)
print(i_love_python[:])             # Full Data

print(i_love_python[0::1])          # Full Data
print(i_love_python[::1])           # Full Data

# Steps
print(i_love_python[::2])           # ILv yhn
print(i_love_python[::3])           # ILv yhn
