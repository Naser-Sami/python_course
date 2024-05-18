# --------------------------
# -- Iterable vs Iterator --
# --------------------------
# Iterable
# [1] Object Contains Data That Can Be Iterated Upon
# [2] Examples (String, List, Set, Tuple, Dictionary)
# ------------------------------------------
# Iterator
# [1] Object Used To Iterate Over Iterable Using next() Method Return 1 Element At A Time
# [2] You Can Generate Iterator From Iterable When Using iter() Method
# [3] For Loop Already Calls iter() Method on The Iterable Behind The Scene
# [4] Gives "StopIteration" If There's No Next Element
# -----------------------------------------------------------


name = "Naser"
for letter in name:
    print(letter, end=" ")

print('\n' + '*' * 20)

numbers = [1, 2, 3, 4]
for num in numbers:
    print(num, end=", ")

print('\n' + '*' * 20)

to_iterator = iter(name)
print(next(to_iterator))
# print(next(to_iterator))
# print(next(to_iterator))
# print(next(to_iterator))
# print(next(to_iterator))
# print(next(to_iterator))    # StopIteration

print('\n' + '*' * 20)

for l in "Naser":   # automatically convert to iter("Naser")
    print(l, end=" ")
