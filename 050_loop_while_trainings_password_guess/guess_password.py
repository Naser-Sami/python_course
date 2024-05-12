# ----------------------------
# -- Loop => While Training --
# -- Simple Password Guess --
# ----------------------------

tries: int = 4
password: str = 'password'
confirm_password: str = input("Enter your password? ")

while confirm_password != password:
    tries -= 1
    print(f"Wrong password, {'Last chance' if tries == 0 else f'{tries} chance left'}")
    confirm_password: str = input("Enter your password? ")

    if tries == 0:
        print("Try again later.")
        break

else:
    print("Correct password.")
