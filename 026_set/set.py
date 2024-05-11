# -----------------------------
# -- Set --
# ---------
# [1] Set Items Are Enclosed in Curly Braces
# [2] Set Items Are Not Ordered And Not Indexed
# [3] Set Indexing and Slicing Can't Be Done
# [4] Set Has Only Immutable Data Types (Numbers, Strings, Tuples) List and Dict Are Not
# [5] Set Items Is Unique
# -----------------------------

# Not Ordered And Not Indexed
set_one = {"Naser", "Sami", 100}
print(set_one)
# Indexing
# print(set_one[0])   # error

# Slicing
tuple_one = (1, 2, 3, 4, 5)
tuple_two = {1, 2, 3, 4, 5}
print(tuple_one[0: 3])
# print(tuple_two[0: 3])    # error


# Has Only Immutable Data Types
# mySetThree = {"Osama", 100, 100.5, True, [1, 2, 3]} # unshakable type: 'list'
set_three = {"Osama", 100, 100.5, True, (1, 2, 3)}
print(set_three)


# Items are unique
set_four = {1, 2, "Osama", "One", "Osama", 1}
print(set_four)
