bought_food_kg = int(input())
bought_food_g = bought_food_kg * 1000
total_food_eaten = 0
while True:
    command = input()
    if command == 'Adopted':
        break
    else:
        total_food_eaten += int(command)
diff = abs(total_food_eaten - bought_food_g)
if total_food_eaten <= bought_food_g:
    print(f"Food is enough! Leftovers: {diff} grams.")
else:
    print(f"Food is not enough. You need {diff} grams more.")

