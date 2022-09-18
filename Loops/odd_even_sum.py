numbers = int(input())
sum_1 = 0
sum_2 = 0
for num in range(numbers):
    current_number = int(input())
    if num % 2 == 0:
        sum_1 += current_number
    else:
        sum_2 += current_number
total_sum = sum_1 + sum_2
diff = abs(sum_1 - sum_2)
if sum_1 == sum_2:
    print(f"Yes")
    print(f"Sum = {sum_1}")
else:
    print(f"No")
    print(f"Diff = {diff}")