import math

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mult(a,b):
    return a*b

def div(a,b):
    return a/b

def log(a):
    if a <= 0:
        raise ValueError("Error")
    return math.log(a)

def square(a):
    return a*a

def sin(a):
    return math.sin(a)

def cos(a):
    return math.cos(a)

def sqrt(a):
    if a < 0:
        raise ValueError("Error")
    return math.sqrt(a)

def percent(a,b):
    if b == 0:
        raise ValueError("Error")
    return (a / 100.0) * b