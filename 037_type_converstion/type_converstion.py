# ---------------------
# -- Type Conversion --
# ----------------------

# str()
a = 10
# b = 10.0
print(type(a))
print(type(str(a)))

print("=" * 40)

b = "Naser"                 # string
c = [1, 2, 3, 4, 5]         # list
d = {"A", "B", "C"}         # set
e = {"A": 1, "B": 2}        # dictionary
f = (1, 2, 3, 4, 5)         # tuple

# convert to tuple()
print(tuple(b))
print(tuple(c))
print(tuple(d))
print(tuple(e))

print("=" * 40)

# convert to list()
print(list(b))
print(list(d))
print(list(e))
print(list(f))

print("=" * 40)

# convert to set()
print(set(b))
print(set(c))
print(set(e))
print(set(f))

print("=" * 40)

# convert to dict()
# print(dict(b))
# print(dict(c))
# print(dict(d))
# print(dict(f))
d = (("A", 1), ("B", 2), ("C", 3))  # Tuple
e = [["One", 1], ["Two", 2], ["Three", 3]]  # List

print(dict(d))
print(dict(e))
