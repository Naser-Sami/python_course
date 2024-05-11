# --------------------
# --  Control Flow  --
# -- If, Elif, Else --
# -- Make Decisions --
# --------------------

user_name = input("Enter your name: ")
country = input("Enter your country: ")
course_name = "Python Course"
course_price = 100
course_discount = 0


# if condition:
if country == "Egypt":
    course_discount = 50
    print(f"Discount for country {country} is {course_discount}")
    print(f"Hello, {user_name} the course \"{course_name}\" price is: ${course_price - course_discount}")
elif country == "KSA":
    course_discount = 10
    print(f"Discount for country {country} is {course_discount}")
    print(f"Hello, {user_name} the course \"{course_name}\" price is: ${course_price - course_discount}")
else:
    course_discount = 30
    print(f"Discount for country {country} is {course_discount}")
    print(f"Hello, {user_name} the course \"{course_name}\" price is: ${course_price - course_discount}")
