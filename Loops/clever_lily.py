years = int(input())
washing_machine_price = float(input())
money_per_toy = int(input())
money_per_birthday = 0
number_of_toys = 0
saved_money = 0

for num in range(1, years + 1):
    if num % 2 != 0:
        number_of_toys += 1
    else:
        money_per_birthday += 10
        saved_money += money_per_birthday - 1


saved_money += number_of_toys * money_per_toy
diff = abs(saved_money - washing_machine_price)
if saved_money >= washing_machine_price:
    print(f"Yes! {diff:.2f}")
else:
    print(f"No! {diff:.2f}")

