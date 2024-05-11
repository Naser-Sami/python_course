# ------------------------
# -- Dictionary Methods --
# ------------------------

# setdefault()

user = {
  "name": "Naser"
}
print(user)
print(user.setdefault("name", "Osama"))
print(user.setdefault("age", 29))
print(user)

print("=" * 40)

# popitem()

member = {
  "name": "Naser",
  "skill": "PS4"
}
print(member)
member.update({"age": 29})
print(member.popitem())

print("=" * 40)


# items()

view = {
  "name": "Osama",
  "skill": "XBox"
}

allItems = view.items()
print(view)
view["age"] = 29

print(allItems)

print("=" * 40)


# fromkeys()

a = ('MyKeyOne', 'MyKeyTwo', 'MyKeyThree')
b = "X"

print(dict.fromkeys(a, b))
