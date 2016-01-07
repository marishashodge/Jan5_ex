
def add(num):
    total = 0
    for k, v in num.items():
        total += int(v)
    return total


def subtract(num):
    total = int(num["num1"]) * 2
    for k, v in num.items():
        total -= int(v)
    return total

def multiply(num):
    total = int(num["num1"])
    for k, v in num.items():
        total *= int(v)
    return total

def divide(num):
    total = int(num["num1"])
    for k, v in num.items():
        total /= int(v)
    return total

def square(num1):
    return num1 ** 2

def cube(num1):
    return num1 ** 3

def power(num1, num2):
    return num1 ** num2

def mod(num1, num2):
    return num1 % num2