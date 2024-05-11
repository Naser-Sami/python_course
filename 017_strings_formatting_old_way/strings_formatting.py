# ------------------------
# -- Strings Formatting --
# ------------------------

name = "Naser"
age = 36
language = "Python"
rank = 10

print("My Name is: " + name)
# print("My Name is: " + name + " and My Age is: " + age) # Type Error

# %s => String
# %d => Number
# %f => Float
print("My Name is: %s" % "Naser")
print("My Name is: %s" % name)
print("My Name is: %s and My Age is: %d" % (name, age))
print("My Name is: %s and My Age is: %d and My Rank is: %f" % (name, age, rank))
print("My Name is %s Iam %s Developer With %d Years Exp" % (name, language, rank))

# Control Floating Point Number
myNumber = 10
print("My Number is: %d" % myNumber)
print("My Number is: %f" % myNumber)
print("My Number is: %.2f" % myNumber)

# Truncate String
myLongString = "Hello Peoples of Elzero Web School I Love You All"
print("Message is %s" % myLongString)
print("Message is %.5s" % myLongString)
