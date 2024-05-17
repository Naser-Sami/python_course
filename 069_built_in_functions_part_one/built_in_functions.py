# ------------------------
# -- Built In Functions --
# ------------------------
# all()
# any()
# bin()
# id()
# ------------------------

# x = [1, 2, 3, 4, 5, 6, False]     # False
# x = [1, 2, 3, 4, 5, 6, []]        # False
x = [1, 2, 3, 4, 5, 6]              # True
if all(x):
    print("All elements are True")
else:
    print("At least there's one element False")


y = [0, False, []]               # False ( 0 , [] , '', False ) -> False
# y = [1, 2, 3, 4, 5]              # True
if any(y):
    print("At least there's one element True")
else:
    print("All elements are False")


# bin() -> Convert to binary
print(bin(100))


a = 1
b = 2

print(id(a))
print(id(b))
