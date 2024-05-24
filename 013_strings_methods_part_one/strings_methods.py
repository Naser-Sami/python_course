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


def domain_get(email):
    try:
        # Split the email at the '@' character and return the second part
        domain = email.split("@")[1]
        return domain
    except IndexError:
        # Handle the case where there is no '@' in the email
        return "Invalid Email Address"


print(domain_get('user@domain.com'))


def findDog(text : str) -> bool:
    if text.__contains__('dog'):
        return True
    else:
        return False


print(findDog('Is there a dog here?'))

count = 0


def count_dog(text: str) -> int:
    global count
    count += text.lower().split().count('dog')

    return count


print(count_dog('This dog runs faster than the other dog dude!'))
