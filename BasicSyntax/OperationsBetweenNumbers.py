num1 = int(input())
num2 = int(input())
operation = input()
result = 0

if operation == '+':
    result = num1 + num2
    if result % 2 == 0:
        print(f"{num1} {operation} {num2} = {result} - even")
    else:
        print(f"{num1} {operation} {num2} = {result} - odd")


if operation == '-':
    result = num1 - num2
    if result % 2 == 0:
        print(f"{num1} {operation} {num2} = {result} - even")
    else:
        print(f"{num1} {operation} {num2} = {result} - odd")

if operation == '*':
    result = num1 * num2
    if result % 2 == 0:
        print(f"{num1} {operation} {num2} = {result} - even")
    else:
        print(f"{num1} {operation} {num2} = {result} - odd")

if operation == '/' and num2 != 0:
    result = num1 / num2
    print(f"{num1} {operation} {num2} = {result:.2f}")

if operation == '%' and num2 != 0:
    result = num1 % num2
    print(f"{num1} {operation} {num2} = {result}")

if (operation == '%' or operation == '/') and num2 == 0:
    print(f"Cannot divide {num1} by zero")
