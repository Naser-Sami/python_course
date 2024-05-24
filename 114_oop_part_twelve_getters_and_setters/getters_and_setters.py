# ------------------------------------------------------
# -- Object Oriented Programming => Getters & Setters --
# ------------------------------------------------------

class Member:
    def __init__(self, name):
        self.__name = name  # private

    def say_hello(self):
        return f"Hello {self.__name}"

    def get_name(self):  # getter
        return self.__name

    def set_name(self, new_name):  # setter
        self.__name = new_name


one = Member("Naser")
# one._Member__name = "Sayed"
# print(one._Member__name)
print(one.get_name())
one.set_name("Sami")
print(one.get_name())
