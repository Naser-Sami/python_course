# ---------------------------
# -- Break, Continue, Pass --
# ---------------------------

numbers = [1, 2, 3, 5, 7, 10, 13, 14, 15, 19]


# Continue
for number in numbers:
    if number == 13:
        continue
    print(number)

print("=" * 20)


# Break
for number in numbers:
    if number == 13:
        break
    print(number)

print("=" * 20)


# Pass
for number in numbers:
    if number == 13:
        pass
    print(number)
