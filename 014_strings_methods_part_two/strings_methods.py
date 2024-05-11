# ---------------------
# -- Strings Methods --
# ---------------------

# split() rsplit()

a = "I Love Python and FLUTTER and MySQL"
print(type(a.split()))      # list
print(a.split())

b = "I-Love-Python-and-FLUTTER-and-MySQL"
print(b.split("-"))

c = "I-Love-Python-and-FLUTTER-and-MySQL"
print(c.split("-", 3))

d = "I-Love-Python-and-FLUTTER-and-MySQL"
print(d.rsplit("-", 3))

# center()
my_name = "Naser"
print(my_name.center(9))    # spaces
print(my_name.center(9, "#"))    # hashes

# count()
my_name = "Naser Sami"
print(my_name.count('a'))
f = "I Love Python and PHP Because PHP is Easy"
print(f.count("PHP"))  # 2 PHP Words
print(f.count("PHP", 0, 25))  # Only One PHP Word

print()

# swapcase()
g = "I Love Python"
h = "i lOVE pYTHON"

print(g.swapcase())
print(h.swapcase())

print()

# startswith()
i = "I Love Python"
print(i.startswith("I"))
print(i.startswith("S"))
print(i.startswith("P", 7, 12))

# endswith()
j = "I Love Python"
print(j.endswith("n"))
print(j.endswith("S"))
print(j.endswith("e", 2, 6))
