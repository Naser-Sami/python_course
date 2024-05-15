# ------------------------
# -- Function => lambda --
# -- Anonymous Function --
# ------------------------
# [1] It Has No Name
# [2] You Can Call It Inline Without Defining It
# [3] You Can Use It In Return Data From Another Function
# [4] Lambda Used For Simple Functions and Def Handle The Large Tasks
# [5] Lambda is One Single Expression not Block Of Code
# [6] Lambda Type is Function
# -------------------------------------------------------------------

def say_hello(name: str, age : int): return f"Hello, {name}, your age is {age}"


# lambda
hello = lambda name, age : f"Hello, {name}, your age is {age}"


print(say_hello('Naser', 29))
print(hello('Naser', 29))

print(say_hello.__name__)
print(hello.__name__)
print(type(hello))
