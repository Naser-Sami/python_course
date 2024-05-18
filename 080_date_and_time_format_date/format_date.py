# ----------------------------------
# -- Date and Time => Format Date --
# ----------------------------------
# https://strftime.org/
# ---------------------

import datetime as dt

birthday = dt.datetime(1994, 9, 13)
print(birthday)
print(birthday.strftime("%a"))
print(birthday.strftime("%A"))
print(birthday.strftime("%b"))
print(birthday.strftime("%B"))

print(birthday.strftime("%d %B %Y"))
print(birthday.strftime("%d, %B, %Y"))
print(birthday.strftime("%d/%B/%Y"))
print(birthday.strftime("%d - %B - %Y"))
print(birthday.strftime("%B - %Y"))
