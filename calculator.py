f_number = float(input("What's the first number? "))
pick_operation = input("Pick an operation (+ - * /) ")
l_number = float(input("What's the next number? "))

keep_calculating = True

def add(a, b):
    sum = a + b
    return sum

def sub(a, b):
    difference = a - b
    return difference

def multiply(a, b):
    product = a * b
    return product

def divide(a, b):
    quotient = a / b
    return quotient

def cont_calc(operation):
    global keep_calculating
    global f_number
    global pick_operation
    global l_number
    y_n = input(f"Type 'y' to continue calculating with {operation}, or type 'n' to start a new calculation: ")
    if y_n == "n":
        keep_calculating = False
    elif y_n == "y":
        f_number = operation
        pick_operation = input("Pick an operation (+ - * /) ")
        l_number = float(input("What's the next number? "))


while keep_calculating == True:
    if pick_operation == "+":
        addition = add(f_number, l_number)
        print(f"{f_number} {pick_operation} {l_number} = {addition}")
        cont_calc(addition)
    elif pick_operation == "-":
        subtraction = sub(f_number, l_number)
        print(f"{f_number} {pick_operation} {l_number} = {subtraction}")
        cont_calc(subtraction)
    elif pick_operation == "*":
        multiplication = multiply(f_number, l_number)
        print(f"{f_number} {pick_operation} {l_number} = {multiplication}")
        cont_calc(multiplication)
    elif pick_operation == "/":
        division = divide(f_number, l_number)
        print(f"{f_number} {pick_operation} {l_number} = {division}")
        cont_calc(division)
    else:
        print("That is not a valid operation")
        break