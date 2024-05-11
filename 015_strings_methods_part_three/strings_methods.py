# ---------------------
# -- Strings Methods --
# ---------------------

# index(sub-string, start, end)
text = "I love python"
print(text.index('p'))
print(text.index('p', 0, 10))

# if the index didn't find, the index method will through an error
# print(text.index('p', 0, 5))


# find(sub-string, start, end)
print(text.find('p'))
# if the index didn't find, the find method will return -1
print(text.find('p', 0, 5))


# rjust(Width, Fill Char) ljust(Width, Fill Char)
c = "Naser"
print(c.rjust(10))
print(c.rjust(10, "#"))

d = "Naser"
print(d.ljust(10))
print(d.ljust(10, "#"))


# splitlines()
e = """First Line
Second Line
Third Line"""
print(e)
print(e.splitlines())

f = "First Line\nSecond Line\nThird Line"
print(f.splitlines())


# expandtabs()
g = "Hello\tWorld\tI\tLove\tPython"
print(g.expandtabs(2))

one = "I Love Python And 3G"
two = "I Love Python And 3g"
print(one.istitle())
print(two.istitle())


three = " "
four = ""
print(three.isspace())
print(four.isspace())

five = 'i love python'
six = 'I Love Python'
print(five.islower())
print(six.islower())


five = 'i love python'
six = 'I Love Python'
print(five.islower())
print(six.islower())

seven = "osama_elzero"
eight = "OsamaElzero100"
nine = "Osama--Elzero100"

print(seven.isidentifier())
print(eight.isidentifier())
print(nine.isidentifier())

x = "AaaaaBbbbbb"
y = "AaaaaBbbbbb111"
print(x.isalpha())
print(y.isalpha())

u = "AaaaaBbbbbb"
z = "AaaaaBbbbbb111"
print(u.isalnum())
print(z.isalnum())

