
def add(num):
    value = 0
    for x in num:
        value += int(x)
    return value


def subtract(num):
    value = int(num[0]) * 2
    for x in num:
        value -= int(x)
    return value

def multiply(num):
    value = 1
    for x in num:
        value *= int(x)
    return value

def divide(num):
    num1 = float(num[0])
    for x in range(len(num)-1):
        value = float(num1) / float(num[x+1])
        num1 = value
    return value

def square(num1):
    return num1 ** 2

def cube(num1):
    return num1 ** 3

def power(num1, num2):
    return num1 ** num2

def mod(num1, num2):
    return num1 % num2