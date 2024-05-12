# ---------------------------------------
# -- Function Parameters And Arguments --
# ---------------------------------------

a, b, c = "Naser", "Sami", "Ebedio"

# print(f"Hello {a}")
# print(f"Hello {b}")
# print(f"Hello {c}")

# def                   -> Function keyword [ Define ]
# greeting              -> Function name
# name                  -> Parameter


def greeting(name):
    return f"Hello, {name}"


greet = greeting(a)
print(greet)
print(greeting(b))


def addition(n1, n2):
    if n1 != int or n2 != int:
        return "Only Integers Allowed"
    else:
        return int(n1) + int(n2)


print(addition(20, 40))


def full_name(first, middle, last):
    print(f"Hello {first.strip().capitalize()} {middle.upper():.1s} {last.capitalize()}")


full_name("   Naser   ", 'Sami', "Ebedo")
