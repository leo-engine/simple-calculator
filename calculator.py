# calculator.py
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero!"
    return x / y

def calculator():
    print("Simple Calculator")
    print("Operations: +, -, *, /")
    print("Enter 'quit' to exit\n")
    
    while True:
        num1 = input("Enter first number (or 'quit'): ")
        if num1.lower() == 'quit':
            break
            
        try:
            num1 = float(num1)
        except ValueError:
            print("Invalid number!")
            continue
            
        operation = input("Enter operation (+, -, *, /): ")
        if operation not in ['+', '-', '*', '/']:
            print("Invalid operation!")
            continue
            
        num2 = input("Enter second number: ")
        try:
            num2 = float(num2)
        except ValueError:
            print("Invalid number!")
            continue
        
        if operation == '+':
            result = add(num1, num2)
        elif operation == '-':
            result = subtract(num1, num2)
        elif operation == '*':
            result

