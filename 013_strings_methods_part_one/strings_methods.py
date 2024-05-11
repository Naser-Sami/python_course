# ---------------------
# -- Strings Methods --
# ---------------------

i_love_python = "I Love Python"
print(len(i_love_python))

# strip() rstrip() lstrip()
i_love_python = "   I Love Python   "
print(len(i_love_python))
print(i_love_python.strip() + "and length is: " + len(i_love_python).__str__())
print(i_love_python.rstrip())
print(i_love_python.lstrip())

print()

# strip() rstrip() lstrip()
# with value
a = "#####I Love Python####"
print(a.strip("#"))
print(a.rstrip("#"))
print(a.lstrip("#"))

a = "@#@#@#I Love Python@#@#@#"
print(a.strip("@#"))
print(a.rstrip("@#"))
print(a.lstrip("@#"))

# title()
b = "I Love 2d Graphics and 3g Technology and python"
print(b.title())

# capitalize()
b = "I Love 2d Graphics and 3g Technology and python"
print(b.capitalize())

# zfill (zero fill)
c, d, e, f = "1", "11", "111", "1111"
zero_fill = 4
print(c)
print(d)
print(e)
print(f)

print(c.zfill(zero_fill))
print(d.zfill(zero_fill))
print(e.zfill(zero_fill))
print(f.zfill(zero_fill))

print()

# upper()
g = "naser"
print(g.upper())

# lower()
h = "NasER"
print(h.lower())
