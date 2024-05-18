# -------------------------
# -- Decorators => Intro --
# -------------------------
# [1] Sometimes Called Meta-Programming
# [2] Everything in Python is Object Even Functions
# [3] Decorator Take A Function and Add Some Functionality and Return It
# [4] Decorator Wrap Another Function and Enhance Their Behavior
# [5] Decorator is Higher Order Function (Function Accept Function As Parameter)
# ----------------------------------------------------------------------

def decorators(func):
    def nested_method():
        print("*" * 20, end="\n\n")
        func()
        print("\n" + "*" * 20, end="\n\n")

    return nested_method


@decorators
def greeting():
    print("Welcome!")


# print(decorators(greeting()))
greeting()
