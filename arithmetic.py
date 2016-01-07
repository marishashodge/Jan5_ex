
def add(num):
    return reduce(lambda x,y: float(x) + float(y), num)

def subtract(num):
    return reduce(lambda x,y: float(x) - float(y), num)

def multiply(num):
    return reduce(lambda x,y: float(x) * float(y), num)

def divide(num):
    return reduce(lambda x,y: float(x) / float(y), num)

def square(num):
    return float(num[0]) ** 2

def cube(num):
    return float(num[0]) ** 3

def power(num):
    return reduce(lambda x,y: float(x) ** float(y), num)

def mod(num):
    return reduce(lambda x,y: float(x) % float(y), num)
