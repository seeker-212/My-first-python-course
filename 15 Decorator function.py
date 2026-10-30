def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2): 
    return n1 / n2

def calculate(calc, n1, n2):
    return calc(n1, n2)

res = calculate(add, 5, 3)
print(res)

