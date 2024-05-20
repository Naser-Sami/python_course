# -----------------------------------
# --      Exceptions Handling      --
# -- Try | Except | Else | Finally --
# -----------------------------------
# Try     => Test The Code For Errors
# Except  => Handle The Errors
# ----------------------------
# Else    => If No Errors
# Finally => Run The Code
# ------------------------

number = int(input("Write Your Age: "))

print(number)
print(type(number))

try:  # Try The Code and Test Errors
    number = int(input("Write Your Age: "))
    print("Good, This Is Integer From Try")

except:  # Handle The Errors If Its Found
    print("Bad, This is Not Integer")

else:  # If There's No Errors
    print("Good, This Is Integer From Else")

finally:
    print("Print From Finally Whatever Happens")

try:
    # print(10 / 0)
    # print(x)
    print(int("Hello"))
except ZeroDivisionError:
    print("Cant Divide")

except NameError:
    print("Identifier Not Found")

except ValueError:
    print("Value Error Elzero")

except:
    print("Error Happens")


################################################

# Bad Practice: Bare except

def risky_function():
    print("")


try:
    # Some risky code
    risky_function()
except:
    print("An error occurred")

# Better Practice: Specific Exception Handling
try:
    # Some risky code
    risky_function()
except ValueError as e:
    print(f"A ValueError occurred: {e}")
except TypeError as e:
    print(f"A TypeError occurred: {e}")
except Exception as e:
    # This is a catch-all for other exceptions
    print(f"An unexpected error occurred: {e}")
else:  # If There's No Errors
    print("No errors.")
finally:
    print("Print From Finally Whatever Happens")
