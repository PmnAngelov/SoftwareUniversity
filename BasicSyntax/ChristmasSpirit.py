allowed_quantity = int(input())
days_left = int(input())
days_passed= 0
christmas_spirit = 0
money_spent = 0

ornament_set = 2
tree_skirt = 5
tree_garlands = 3
tree_lights = 15

for day in range(days_left, 0 , -1):
    days_passed += 1
    if days_passed % 11 == 0:
        allowed_quantity = allowed_quantity + 2
    if days_passed % 2 == 0:
        money_spent += ornament_set * allowed_quantity
        christmas_spirit += 5
    if days_passed % 3 == 0:
        money_spent += tree_skirt * allowed_quantity + tree_garlands * allowed_quantity
        christmas_spirit += 13
    if days_passed % 5 == 0:
        money_spent += tree_lights * allowed_quantity
        christmas_spirit += 17
        if days_passed % 3 == 0:
            christmas_spirit += 30
    if days_passed % 10 == 0:
        christmas_spirit -= 20
        money_spent += tree_skirt + tree_garlands + tree_lights
        if days_passed == days_left:
            christmas_spirit -= 30

print(f"Total cost: {money_spent}")
print(f"Total spirit: {christmas_spirit}")

