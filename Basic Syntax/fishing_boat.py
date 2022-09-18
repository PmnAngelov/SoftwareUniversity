budget = int(input())
season = input()
fishermen = int(input())
base_price = 0

if season == 'Spring':
    base_price = 3000
elif season == 'Summer' or season == 'Autumn':
    base_price = 4200
elif season == 'Winter':
    base_price = 2600

if fishermen <= 6:
    base_price *= 0.90
elif 6 < fishermen <= 11:
    base_price *= 0.85
elif fishermen > 11:
    base_price *= 0.75

if season != 'Autumn' and fishermen % 2 == 0:
    base_price *= 0.95

difference = abs(base_price - budget)

if budget >= base_price:
    print(f"Yes! You have {difference:.2f} leva left.")
else:
    print(f"Not enough money! You need {difference:.2f} leva.")
