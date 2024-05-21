# ----------------------------------------------------------
# -- Object Oriented Programming => Class Syntax and Info --
# ----------------------------------------------------------
# [01] Class is The Blueprint Or Constructor Of The Object
# [02] Class Instantiate Means Create Instance of A Class
# [03] Instance => Objects Created From Class And Have Their Methods and Attributes
# [04] Class Defined With Keyword class
# [05] Class Name Written With PascalCase [UpperCamelCase] Style
# [06] Class May Contain Methods and Attributes
# [07] When Creating Object Python Look For The Built In __init__ Method
# [08] __init__ Method Called Every Time You Create an Object From Class
# [09] __init__ Method Is Initialize The Data For The Object
# [10] Any Method With Two Underscore in The Start and End Called Dunder or Magic Method
# [11] self Refer To The Current Instance Created From The Class And Must Be First Param
# [12] self Can Be Named Anything
# [13] In Python You Dont Need To Call new() Keyword To Create Object
# -------------------------------------------------------------------

# Syntax
# class Name:
#     Constructor => Do Instantiation [ Create Instance From A Class ]
#     Each Instance Is Separate Object
#     def __init__(self, other_data)
#         Body Of Function

class ExClass:
    pass


class ClassName:
    def __init__(self):
        pass


class Member:
    def __init__(self):
        print("A new member has been added")


m1 = Member()
Member()
Member()

print(dir(Member))
print(dir(str))
print(m1.__class__)

my_dictionary = {
  'name': "Naser",
  'age': 29,
  'monthly_salary': 50000,
  'yearly_salary': ''  # Something
}
