import sys

numbers = int(input())
sum = 0
max_number = -sys.maxsize

for num in range(numbers):
    current_number = int(input())
    sum += current_number
    if current_number > max_number:
        max_number = current_number
        
sum = sum - max_number
if sum == max_number:
    print(f"Yes")
    print(f"Sum = {max_number}")
else:
    diff = abs(sum - max_number)
    print(f"No")
    print(f"Diff = {diff}")

