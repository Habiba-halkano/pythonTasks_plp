# Instructions:

# Basic Calculator Program

# Create a simple Python program that asks the user to input two numbers and a mathematical operation (addition, subtraction, multiplication, or division).
# Perform the operation based on the user's input and print the result.
# Example: If a user inputs 10, 5, and +, your program should display 10 + 5 = 15.

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
