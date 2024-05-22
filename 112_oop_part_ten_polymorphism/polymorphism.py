# -------------------------------------------------
# -- Object Oriented Programming => Polymorphism --
# -------------------------------------------------


# Polymorphism Examples on the Print Method

# n1 = 10
# n2 = 20
#
# print(n1 + n2)
#
# s1 = "Hello"
# s2 = "Python"
#
# print(s1 + " " + s2)
#
# print(len([1, 2, 3, 4, 5]))
# print(len("Naser Ebedo"))
# print(len({"Key_One": 1, "Key_Two": 2}))


class A:
    def do_something(self):
        # print("Hello from class A")
        raise NotImplementedError("Derived Class Must Implement This Method")


class B(A):
    pass
    # def do_something(self):
    #     print("Hello from class B")


class C(A):
    def do_something(self):
        print("Hello from class C")


new_instance = C()
new_instance.do_something()
