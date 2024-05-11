# ---------------------------
# -- Practical Slice Email --
# ---------------------------

# email = "naser_ebedo@icloud.com"
# print(email[0:5])
# index = email.index('@')
# print(index)
# print(email[0:index])

name = input("Enter you name: ").strip().capitalize()
email = input("Enter you email: ").strip()
print(f"Hello, {name}, with email {email}")

user_name = email[:email.index('@')]
website = email[email.index('@') + 1:]
print(f"Your username is {user_name}, and your website is: {website}")
