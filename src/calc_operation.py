def sum(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

def power(n1, n2):
    return n1 ** n2

def root(n1, n2):
    return n1 ** (1/n2)

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def mod(n1, n2):
    return n1 % n2