# ----------------------------------
# -- Built In Functions => Filter --
# ----------------------------------
# [1] Filter Take A Function + Iterator
# [2] Filter Run A Function On Every Element
# [3] The Function Can Be Pre-Defined Function or Lambda Function
# [4] Filter Out All Elements For Which The Function Returns True
# [5] The Function Need To Return Boolean Value
# ---------------------------------------------------------------

# Example 1

def check_number(num: float):
    if num > 10:
        return num
    if num == 0:
        return True     # I can't return num here because 0 is False


numbers = [0, 0, 1, 19, 10, 20, 100, 5, 0]
result = filter(check_number, numbers)

for number in result:
    print(number)


# Example 2

print("=" * 20)


def check_name(name: str):
    return name.startswith("N")


names = ["Naser", "Nader", "Hassan", "Najeeb", "Osama"]
name_result = filter(check_name, names)

for name in name_result:
    print(name)


# Example 3

print("=" * 20)

names.append("Yusuf")
name_result = filter((lambda name : name.startswith("Y")), names)

for n in name_result:
    print(n)
