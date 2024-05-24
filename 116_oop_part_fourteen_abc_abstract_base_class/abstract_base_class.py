# ----------------------------------------------------------------
# -- Object Oriented Programming => ABCs => Abstract Base Class --
# ----------------------------------------------------------------
# - Class Called Abstract Class If it Has One or More Abstract Methods
# - abc module in Python Provides Infrastructure for Defining Custom Abstract Base Classes.
# - By Adding @abstractmethod Decorator on The Methods
# - ABCMeta Class Is a MetaClass Used For Defining Abstract Base Class
# --------------------------------------------------------------------

from abc import ABCMeta, abstractmethod


class Programing(metaclass=ABCMeta):
    @abstractmethod
    def has_oop(self) -> bool:
        pass


class Python(Programing):

    def has_oop(self) -> bool:
        return True


class Pascal(Programing):

    def has_oop(self) -> bool:
        return False


python = Python()
print(python.has_oop())

pascal = Pascal()
print(pascal.has_oop())
