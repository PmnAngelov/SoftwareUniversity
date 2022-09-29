num = int(input())
numbers = []
answer = []
for a in range(num):
    current_number = int(input())
    numbers.append(current_number)

command = str(input())
for number in numbers:
    if command == "positive":
        if number >= 0:
            answer.append(number)
    if command == "negative":
        if number < 0:
            answer.append(number)
    if command == "even":
        if number % 2 == 0:
            answer.append(number)
    if command == "odd":
        if number % 2 != 0:
            answer.append(number)
print(answer)
