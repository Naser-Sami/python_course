# ---------------------------------------------------------
# -- Object Oriented Programming => Multiple Inheritance --
# ---------------------------------------------------------

class BaseOne:
    def __init__(self):
        print("Base One Class")

    def print_one(self) -> None:
        print("One")


class BaseTwo:
    def __init__(self):
        print("Base Two Class")

    def print_two(self) -> None:
        print("Two")


class Derived(BaseOne, BaseTwo):
    pass


class Derived2(BaseTwo, BaseOne):
    pass


var = Derived()
print(Derived.mro())

var2 = Derived2()
print(Derived2.mro())

print(var.print_one)
print(var.print_two)
var.print_one()
var.print_two()


class Base:
    pass


class DerivedOne(Base):
    pass


class DerivedTwo(DerivedOne):
    pass
