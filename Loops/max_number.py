import sys

max_number = -sys.maxsize
while True:
    current_number = input()
    if current_number == 'Stop':
        break
    elif int(current_number) > max_number:
        max_number = int(current_number)

print(max_number)