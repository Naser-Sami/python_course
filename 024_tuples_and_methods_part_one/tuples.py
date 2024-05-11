# -----------------------------
# -- Tuple --
# -----------
# [1] Tuple Items Are Enclosed in Parentheses
# [2] You Can Remove The Parentheses If You Want
# [3] Tuple Are Ordered To Use Index To Access Item
# [4] Tuple Are Immutable => You Cant Add or Delete
# [5] Tuple Items are Not Unique
# [6] Tuple Can Have Different Data Types
# [7] Operators Used in Strings and Lists Available In Tuples
# -----------------------------

# Tuple Syntax & Type Test
tuple_one = ("Naser", "Sami")
tuple_two = "Naser", "Sami"
print(tuple_one)
print(tuple_two)
print()


# Tuple Indexing
tuple_three = 1, 2, 3, 4, 5
print(tuple_three.index(2))
print()


# Tuple Assign Values
tuple_four = (1, 2, 3, 4, 5)
# tuple_four[2] = "Three"
# print(tuple_four)  # 'tuple' object does not support item assignment


# Tuple Data
tuple_five = ("Osama", "Osama", 1, 2, 3, 100.5, True)
print(tuple_five[1])
print(tuple_five[-1])
