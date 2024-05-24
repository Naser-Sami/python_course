# --------------------------------------------------------
# -- Object Oriented Programming => @Property Decorator --
# --------------------------------------------------------

class Member:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        return f"Hello, {self.name}"

    @property
    def age_in_days(self):
        return self.age * 365


m1 = Member("Naser", 29)
print(m1.name)
print(m1.age)
print(m1.say_hello())
# print(m1.age_in_days()) # error

print(m1.say_hello())  # method
print(m1.age_in_days)  # property
