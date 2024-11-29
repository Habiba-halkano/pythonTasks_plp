def result(a, b, operation):
    if operation == '+':
        result = a + b
        return result
    elif operation == '-':
        result = a - b
        return result
    elif operation == '*':
        result = a * b
        return result
    else:
        result = a / b
        return result

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
operation = input("Enter operation: ")
result = print(result(a, b, operation))