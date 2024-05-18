# ----------------
# -- Generators --
# ----------------
# [1] Generator is a Function With "yield" Keyword Instead of "return"
# [2] It Supports Iteration and Return Generator Iterator By Calling "yield"
# [3] Generator Function Can Have one or More "yield"
# [4] By Using next() It Resume From Where It Called "yield" Not From beginning
# [5] When Called, It's Not Start Automatically; it Only Gives You The Control
# -----------------------------------------------------------------

def my_generator():
    yield 1
    yield 2
    yield 3
    yield 4


gen = my_generator()

print(next(gen), end=" ")
print("Hello From Python")
print(next(gen), end=" ")
print('\n' + '*' * 20)

for number in gen:
    print(number)
