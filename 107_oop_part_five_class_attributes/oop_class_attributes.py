# -----------------------------------------------------
# -- Object Oriented Programming => Class Attributes --
# -----------------------------------------------------
# Class Attributes: Attributes Defined Outside The Constructor
# -----------------------------------------------------------


class Member:

    # Class Attributes -> Defined Outside The Constructor
    not_allowed_names = ["Hell", "Shit", "Baloot"]
    users_num = 0

    # Constructor
    def __init__(self, f_name, m_name, l_name, gender):
        self.first_name = f_name
        self.middle_name = m_name
        self.last_name = l_name
        self.gender = gender

        # increase the number of users for each time constructor create a new instance
        Member.users_num += 1

    def full_name(self):
        if self.first_name in Member.not_allowed_names:
            raise ValueError("Name not allowed")
        else:
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

    def delete_user(self):
        Member.users_num -= 1
        return f"User {self.first_name} deleted."


print(Member.users_num)
member = Member("Sami", "Naser", "Ebedo", "Male")
print(member.get_all_info())
print(Member.users_num)
