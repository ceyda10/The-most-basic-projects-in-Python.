def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

print("Welcome to the calculator project")
print("1. Multiply, 2. Divide")

operation = input("Please select the operation you want to perform:")

if operation == "1":
    number1 = int(input("Enter the first number: "))
    number2 = int(input("Enter the second number: "))
    print("Result:", multiply(number1, number2))

if operation == "2":
    number1 = int(input("Enter the first number: "))
    number2 = int(input("Enter the second number: "))
    print("Result:", divide(number1, number2))
