# ---------------------------
# -- Dictionary --
# ----------------
# [1] Dict Items Are Enclosed in Curly Braces
# [2] Dict Items Contains Key: Value
# [3] Dict Key Need To Be Immutable => (Number, String, Tuple) List Not Allowed
# [4] Dict Value Can Have Any Data Types
# [5] Dict the Key Need To Be Unique
# [6] Dict Is Not Ordered You to Access Its Element With Key
# ----------------------------

# Dictionary
user = {
    "name": "Naser",
    "age": 29,
    "country": "Jordan",
    "skills": ["Dart", "Flutter", "C++", "C#", "Python"],
    "rating": 10.5,
    # "name": "Sami"
}

print(user)
print(user.get('name'))
print(user['skills'])
print(user['skills'][-1])

print("\n ****** \n")

print(user.keys())
print(user.values())
print("\n ****** \n")

# Two-Dimensional Dictionary
languages = {
    "One": {
        "name": "Dart",
        "progress": "95%"
    },
    "Two": {
        "name": "Flutter",
        "progress": "95%"
    },
    "Three": {
        "name": "C++",
        "progress": "50%"
    },
    "Four": {
        "name": "C#",
        "progress": "60%"
    },
    "Five": {
        "name": "Python",
        "progress": "70%"
    },
}

print(languages['Five'])
print(f"{languages['Five']['name']}, {languages['Five']['progress']}")

print(len(languages))
print(len(languages['Four']))


# Create Dictionary From Variables
frameworkOne = {
  "name": "Vuejs",
  "progress": "80%"
}

frameworkTwo = {
  "name": "ReactJs",
  "progress": "80%"
}

frameworkThree = {
  "name": "Angular",
  "progress": "80%"
}

allFramework = {
  "one": frameworkOne,
  "two": frameworkTwo,
  "three": frameworkThree
}

print(allFramework)
