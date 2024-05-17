# ------------------------
# -- Built In Functions --
# ------------------------
# enumerate()
# help()
# reversed()
# ------------------------

# enumerate(iterable, start=0)
my_skills = ["Html", "Css", "Js", "PHP"]

my_skills_with_counter = enumerate(my_skills, 20)

print(type(my_skills_with_counter))

for counter, skill in my_skills_with_counter:
    print(f"{counter} - {skill}")

print("#" * 50)

# help()
print(help(print))

print("#" * 50)

# reversed(iterable)
my_string = "Elzero"

print(reversed(my_string))

for letter in reversed(my_string):
    print(letter)

print("#" * 50)

for s in reversed(my_skills):
    print(s)
