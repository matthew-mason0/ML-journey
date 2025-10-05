def calculate(a, b, operator):
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    elif operator == '/':
        if b == 0:
            return "Error: Division by zero"
        return a / b
    else:
        return "Error: Unkown operator"

# Test cases
print(calculate(10, 5, '+')) # 15

print(calculate(10, 0, '/')) # Error

print(calculate(7, 3, '*')) # 21