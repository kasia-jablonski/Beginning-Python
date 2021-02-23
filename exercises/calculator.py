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
    print(x)
    if (re.match("^-?\d+(\.\d+)?$", x) != None):
        print('----')
        print(x)
        if (re.match("^-?\d+?[.]\d+$", x)):
            return float(x)
        else :
            return int(x)
        print("Should not print")
    else:
        check_type(number)

a = check_type("first")
print(a)
show_operations()
o = input("> ")
while (o not in ['+', '-', '*', '/']):
    show_operations()
    o = input("> ")

print(o)

b = check_type("second")

result = calculate(o)
print("Result is " + str(result))