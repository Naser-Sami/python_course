# --------------------------------------------------------------------
# -- Object Oriented Programming => Instance Attributes and Methods --
# --------------------------------------------------------------------
# Self: Point To Instance Created From Class
# Instance Attributes: Instance Attributes Defined Inside The Constructor
# -----------------------------------------------------------------------
# Instance Methods: Take Self Parameter Which Point To Instance Created From Class
# Instance Methods Can Have More Than One Parameter Like Any Function
# Instance Methods Can Freely Access Attributes And Methods On The Same Object
# Instance Methods Can Access The Class Itself
# -----------------------------------------------------------

# class Member:
#     def __init__(self):
#         self.name = "Naser"
#
#
# m1 = Member()
# m2 = Member()
# m3 = Member()
#
# print(dir(m1))
# print(m1.name)

class Member:
    def __init__(self, f_name, m_name, l_name):
        self.first_name = f_name
        self.middle_name = m_name
        self.last_name = l_name


# m1 = Member("Sami", "Naser", "Ebedo")
# m2 = Member("Naser", "Sami", "Ebedo")
# m3 = Member("Ebedo")

# print(dir(m1))
# print(m1.first_name)
# print(m2.first_name)
# print(m3.name)


class Members:
    def __init__(self, member : Member):
        self.member = member

    def print_members(self):
        print(self.member.first_name)
        print(self.member.middle_name)
        print(self.member.last_name)


members = Members(Member("Sami", "Naser", "Ebedo"))
print(members.print_members())
