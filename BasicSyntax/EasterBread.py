budget = float(input())
money_spent = 0
bread_count = 0
colored_eggs = 0
price_for_1kg_flour = float(input())
price_for_eggs = price_for_1kg_flour * 0.75
price_for_1ltr_milk = price_for_1kg_flour + price_for_1kg_flour * 0.25
price_for_250mg_milk = price_for_1ltr_milk * 0.25

price_for_1_bread = price_for_eggs + price_for_1kg_flour + price_for_250mg_milk

while money_spent < budget:
    bread_count += 1
    money_spent += price_for_1_bread
    colored_eggs += 3
    if bread_count % 3 == 0:
        lost_eggs = bread_count - 2
        colored_eggs -= lost_eggs
    if money_spent + price_for_1_bread > budget:
        break

money_left = abs(budget-money_spent)
print(f"You made {bread_count} loaves of Easter bread! Now you have {colored_eggs} eggs and {money_left:.2f}BGN left.")


