"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic import *

# Your code goes here
def assign_variables(tokens):
    variables = {}
    y = 1

    while y < len(tokens):
        variables["num"+str(y)] = tokens[y]
        y += 1

    return variables

calculator_on = True

while calculator_on:
    userinput = raw_input("Please use the calculator:\n")
    tokens = userinput.split(" ")

    if userinput == "q":
        calculator_on = False

    variables = assign_variables(tokens)

    sign = tokens[0]

    if sign == "+":
        print(add(variables))
    elif sign == "-":
        print(subtract(num1, num2))
    elif sign == "*":
        print(multiply(num1, num2))
    elif sign == "/":
        print(divide(num1, num2))
    elif sign == "square":
        print(square(num1))
    elif sign == "cube":
        print(cube(num1))
    elif sign == "pow":
        print(power(num1, num2))
    elif sign == "mod":
        print(mod(num1, num2))