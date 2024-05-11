# -----------
# -- Tuple --
# -----------

# Tuple With One Element
tuple_one = ("Naser", )
print(type(tuple_one))      # tuple
print(len(tuple_one))
tuple_two = "Naser"
print(type(tuple_two))      # string
print(len(tuple_two))
tuple_two = "Naser",
print(type(tuple_two))      # tuple
print(len(tuple_two))

# Tuple Concatenation
a = (1, 2, 3, 4)
b = (5, 6)

c = a + b
d = a + ("A", "B", True) + b

print(c)
print(d)


# Tuple, List, String Repeat (*)
my_string = "Naser"
my_list = [1, 2]
my_tuple = ("A", "B")

print(f"{my_string} " * 3)
print(my_list * 3)
print(my_tuple * 3)


# Methods => count()
a = (1, 3, 7, 8, 2, 6, 5, 8)
print(a.count(8))


# Methods => index()
b = (1, 3, 7, 8, 2, 6, 5)
# print("The Position of Index Is: " + b.index(7))  # Error
print("The Position of Index Is: {:d}".format(b.index(7)))
print(f"The Position of Index Is: {b.index(7)}")

# Tuple Destruct
a = ("A", "B", 4, "C")
# x, y, z = "A", "B", "C"
x, y, _, z = a

print(x)
print(y)
print(z)
