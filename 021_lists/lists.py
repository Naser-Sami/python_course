# -----------------------------
# -- Lists --
# -----------
# [1] List Items Are Enclosed in Square Brackets
# [2] List Are Ordered To Use Index To Access Item
# [3] List Are Mutable => Add, Delete, Edit
# [4] List Items Is Not Unique
# [5] List Can Have Different Data Types
# -----------------------------

_list_ = ["One", "Two", "One", 1, 100.5, True]

print(_list_)                           # Whole List
print(_list_[1])                        # "Two"
print(_list_[-1])                       # True
print(_list_[-3])                       # 1

print(_list_[1:4])                      # ['Two', 'One', 1]
print(_list_[:4])                       # ['One', 'Two', 'One', 1]
print(_list_[1:])                       # ['Two', 'One', 1, 100.5, True]

print(_list_[::1])                      # ['One', 'Two', 'One', 1, 100.5, True]
print(_list_[::2])                      # ['One', 'One', 100.5]

print(_list_)
_list_[1] = 2
_list_[-1] = False
print(_list_)
_list_[0:3] = ["A"]                     # replace all slices of range from 0:3 (3-1) and add "A"
print(_list_)
