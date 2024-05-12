# -----------------
# -- Loop => For --
# -----------------
# for item in iterable_object :
#   Do Something With Item
# -----------------------------
# item Is A Vairable You Create and Call Whenever You Want
# item refer to the current position and will run and visit all items to the end
# iterable_object => Sequence [ list, tuples, set, dict, string of charcaters, etc ... ]
# ---------------------------------------------------------------


numbers: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for number in numbers:
    if number % 2 == 0:
        print(f'{number} Even number')
    else:
        print(f'{number} Odd number')
else:
    print("Loop has finished.")


name = "Naser"
for letter in name:
    print(f' [ {letter.upper()} ] ')
