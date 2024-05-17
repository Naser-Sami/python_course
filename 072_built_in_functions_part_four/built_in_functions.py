# -------------------------------
# -- Built In Functions => Map --
# -------------------------------
# [1] Map Take A Function + Iterator
# [2] Map Called Map Because It Maps The Function On Every Element
# [3] The Function Can Be Pre-Defined Function or Lambda Function
# ---------------------------------------------------------------

# Use Map With Predefined Function

def formate_text(text : str):
    return f"- {text.strip().capitalize()} -"


texts = ["naser", "sami", "ebedo"]
formated_text = map(formate_text, texts)
print(formated_text)

# for name in formated_text:
#     print(name)


for name in list(formated_text):
    print(name)

print("#" * 50)

# Use Map With Lambda Function
for name in list(map(lambda text : f"- {text.strip().capitalize()} -", texts)):
    print(name)
