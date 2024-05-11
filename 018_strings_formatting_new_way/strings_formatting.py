# ------------------------
# -- Strings Formatting --
# ------------------------
# note: see formatting in last section for version 3.6+

name = 'Naser'
age = 29
rank = 100

msg = "My name is {}, my age is {}, and my RANK is {}".format(name, age, rank)
print(msg)
msg = "My name is {:s}, my age is {:d}, and my RANK is {:.2f}".format(name, age, rank)
print(msg)

# {:s} -> String
# {:d} -> Number
# {:f} -> Float

# Truncate String
welcome_msg = "Welcome to Naser channel!"
print("Welcome message is {}".format(welcome_msg))
print("Welcome message is {:.7s}".format(welcome_msg))

# Money formatting
my_wallet = 500201922
print("My balance in Bank is {}".format(my_wallet))
print("My balance in Bank is {:_d}".format(my_wallet))
print("My balance in Bank is {:,d}".format(my_wallet))

# Rearrange items
a, b, c = "One", "Two", "Three"
print("Hello {} {} {}".format(a, b, c))     # Hello One Two Three
print("Hello {1} {2} {0}".format(a, b, c))  # Hello Two Three One
print("Hello {2} {0} {1}".format(a, b, c))  # Hello Three One Two
print()

x, y, z = 10, 20, 30
print("Hello {} {} {}".format(x, y, z))
print("Hello {1:d} {2:d} {0:d}".format(x, y, z))
print("Hello {2:f} {0:f} {1:f}".format(x, y, z))
print("Hello {2:.2f} {0:.4f} {1:.5f}".format(x, y, z))

# Format in Version 3.6+
myName = "Osama"
myAge = 36

print("My Name is : {myName} and My Age is : {myAge}")
print(f"My Name is : {myName} and My Age is : {myAge}")
