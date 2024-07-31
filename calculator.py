from calculator import add 

def add(x, y):
    return x + y
result = add(1,2) 
print(result) 

def subtract(x, y):
    return x - y
result = subtract (10,7)
print ( result )


def divide(x, y):
    return x / y
result = divide (6,2)
print( result)

def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y

def divide_by_zero():
    result = divide(99, 0)
    print(type(result))
divide_by_zero()

def multiply(x, y):
    return x * y
result = multiply (2,3)
print ( result )

def square(x):
    return x ** 2
result = square (3)
print ( result)

def power(x, y):
   return x ** y
result = power(3,2)
print (result)

def sqrt(x):
    return x ** 0.5
result = sqrt(9)
print (result)
