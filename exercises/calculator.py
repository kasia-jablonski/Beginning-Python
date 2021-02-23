import re

def show_operations():
    print("Select operation: ")
    print("""
    Enter '+' to add
    Enter '-' to subtract
    Enter '*' to multiply
    Enter '/' to divide
    """)

def calculate(x):
    result = 0
    if x == "+":
        result = a + b
    elif x == '-':
        result = a - b
    elif x == '*':
        result = a * b
    elif x == '/':
        result = a / b
    return result

def check_type(number):
    x = input("Enter %s number: " %(number))
    if (re.match("^-?\d+(\.\d+)?$", x) != None):
        if (re.match("^-?\d+?[.]\d+$", x)):
            return float(x)
        else :
            return int(x)
    return None

a = check_type("first")
while (a == None):
    a = check_type("first")

show_operations()
o = input("> ")
while (o not in ['+', '-', '*', '/']):
    show_operations()
    o = input("> ")

b = check_type("second")
while (b == None):
    b = check_type("second")

result = calculate(o)
print("Result is " + str(result))