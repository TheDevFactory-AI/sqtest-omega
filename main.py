def add_numbers(a, b):
    return a + b
def multiply_numbers(a, b):
    return a * b

def divide_numbers(a, b):
    if b == 0:
        return "Error: Cannot divide by zero."
    return a / b
def subtract_numbers(a, b):
    return a - b



result = add_numbers(5, 3)
print("Addition result:", result)

result = subtract_numbers(8, 4)
print("Subtraction result:", result)

result = multiply_numbers(2, 6)
print("Multiplication result:", result)

result = divide_numbers(10, 2)
print("Division result:", result)


#test