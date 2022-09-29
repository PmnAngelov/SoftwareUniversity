numbers = str(input())
listed_numbers = list(numbers)
answer = []

for num in listed_numbers:
    if num is int:
        current = int(num)
        current = current * -1
        answer.append(current)

print(answer)
