# --------------------------------------------
# -- Decorators => Function With Parameters --
# --------------------------------------------

def decorators(func):  # Decorator it can be any function to check any condition
    def nested_method(n1, n2):

        if n1 < 0 or n2 < 0:
            print("One or both of the numbers is less than zero.")

        print("*" * 20, end="\n\n")
        func(n1, n2)
        print("\n" + "*" * 20, end="\n\n")

    return nested_method


def just_print(func):
    def nested_method(n1, n2):
        print("Coming From Decorator Two")
        func(n1, n2)
    return nested_method


@decorators
@just_print
def calculate_two_number(n1, n2):
    print(n1 + n2)


calculate_two_number(10, 20)
