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

class Member:
    def __init__(self, f_name, m_name, l_name, gender):
        self.first_name = f_name
        self.middle_name = m_name
        self.last_name = l_name
        self.gender = gender

    def full_name(self):
        return f"{self.first_name} {self.middle_name} {self.last_name}"

    def hello_method(self):
        if self.gender.lower() == "male":
            return f"Hello Mr. {self.last_name}"
        elif self.gender.lower() == "female":
            return f"Hello Ms. {self.last_name}"
        else:
            return f"Hello, {self.last_name}"

    def get_all_info(self):
        return f"{self.hello_method()}, your full name is: {self.full_name()}"


member = Member("Sami", "Naser", "Ebedo", "Male")
print(member.get_all_info())
