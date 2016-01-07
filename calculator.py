"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic import *

# Your code goes here
calculator_on = True

while calculator_on:
    userinput = raw_input("Please use the calculator:\n")

    if userinput == "q":
        calculator_on = False

    tokens = userinput.split(" ")
    sign = tokens[0]
    
    if len(tokens) == 2:
        num1 = int(tokens[1])
    if len(tokens) == 3:
        num1 = int(tokens[1])
        num2 = int(tokens[2])

    if sign == "+":
        print(add(num1, num2))
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