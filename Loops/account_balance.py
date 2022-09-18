balance = 0
while True:
    current = input()
    if current == 'NoMoreMoney':
        break
    elif float(current) < 0:
        print("Invalid operation!")
        break
    print(f"Increase: {float(current):.2f}")
    balance += float(current)

print(f"Total: {balance:.2f}")