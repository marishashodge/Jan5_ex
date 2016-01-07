"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic import *

import sys

# Your code goes here

calculator_on = True

while calculator_on:
    userinput = raw_input("Please use the calculator:\n")
    tokens = userinput.split(" ")
    sign = tokens.pop(0)
    
    for x in tokens:
        if x.startswith('-') and x[1:].isdigit():
            continue
        if not x.isdigit():
            print "You can only enter numbers between the spaces after the operator."
            sys.exit()

    if sign == "q":
        calculator_on = False

    if sign == "+":
        print(add(tokens))
    elif sign == "-":
        print(subtract(tokens))
    elif sign == "*":
        print(multiply(tokens))
    elif sign == "/":
        print(divide(tokens))
    elif sign == "square":
        print(square(tokens))
    elif sign == "cube":
        print(cube(tokens))
    elif sign == "pow":
        print(power(tokens))
    elif sign == "mod":
        print(mod(tokens))
    else:
        print("That is not a valid input.")
