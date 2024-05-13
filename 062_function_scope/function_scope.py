# --------------------
# -- Function Scope --
# --------------------

# global scope
number1 = 3.14
number2 = 1.618


def function_one():
    global number2

    number1 = 10
    print(f'Print variable from function one scope. number1-> {number1}')

    number2 = 20
    print(f'Print variable from function one scope. number2-> {number2}')


def function_two():
    print(f'Print variable from function two scope. number1-> {number1}')
    print(f'Print variable from function two scope. number2-> {number2}')


print(f'Print variable from global scope. number1-> {number1} and number2-> {number2}\n')
function_one()
function_two()
print(f'\nPrint variable from global scope. number1-> {number1} and number2-> {number2}')
