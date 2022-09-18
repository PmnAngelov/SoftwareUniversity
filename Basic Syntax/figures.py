from math import pi

figure = input()
if figure == 'square':
    num1 = float(input("Please enter the square's side: "))
    area = num1*num1
    print(f"The area of the figure is: {area:.3f}")

elif figure == 'rectangle':
    num1 = float(input("Please enter the rectangle's first side: "))
    num2 = float(input("Please enter the rectangle's second side: "))
    area = num1*num2
    print(f"The area of the figure is: {area:.3f}")

elif figure == 'circle':
    num1 = float(input("Please enter the circle's radius: "))
    area = pi * (num1 ** 2)
    print(f"The area of the figure is: {area:.3f}")

elif figure == 'triangle':
    num1 = float(input("Please enter the triangle's first side: "))
    num2 = float(input("Please enter the triangle's second side: "))
    area = ( num1 * num2 ) / 2
    print(f"The area of the figure is: {area:.3f}")