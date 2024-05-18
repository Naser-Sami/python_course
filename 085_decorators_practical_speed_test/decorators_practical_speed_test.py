# ----------------------------------------
# -- Decorators => Practical Speed Test --
# ----------------------------------------

from time import time


def my_decorator(func):  # Decorator

    def nested_func(*numbers):  # Any Name Its Just For Decoration

        for number in numbers:

            if number < 0:
                print("Beware One Of The Numbers Is Less Than Zero")

        func(*numbers)  # Execute Function

    return nested_func  # Return All Data


@my_decorator
def calculate(n1, n2, n3, n4):
    print(n1 + n2 + n3 + n4)


calculate(-5, 90, 50, 150)


def speed_test(func):
    def wrapper():
        start = time()

        func()

        end = time()

        print(f"Function Running Time Is: {end - start}")

    return wrapper


@speed_test
def big_loop():
    for number in range(1, 20000):
        print(number)


big_loop()
