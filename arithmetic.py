def my_reduce(function, lst):
    value = 0
    for x in lst:
        value = function(value, x)
    return value


def add(num):
    return '{:.2f}'.format(reduce(lambda x,y: float(x) + float(y), num))

def subtract(num):
    return '{:.2f}'.format(reduce(lambda x,y: float(x) - float(y), num))

def multiply(num):
    return '{:.2f}'.format(reduce(lambda x,y: float(x) * float(y), num))

def divide(num):
    return '{:.2f}'.format(reduce(lambda x,y: float(x) / float(y), num))

def square(num):
    return '{:.2f}'.format(float(num[0]) ** 2)

def cube(num):
    return '{:.2f}'.format(float(num[0]) ** 3)

def power(num):
    return '{:.2f}'.format(reduce(lambda x,y: float(x) ** float(y), num))

def mod(num):
    return '{:.2f}'.format(reduce(lambda x,y: float(x) % float(y), num))
