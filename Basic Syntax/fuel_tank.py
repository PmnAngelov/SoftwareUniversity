fuel_type = str(input())
fuel_liters = float(input())
club_card = str(input())
gasoline_per_ltr = 2.22
diesel_per_ltr = 2.33
gas_per_ltr = 0.93

if fuel_type == 'Gasoline' :
    initial_cost = fuel_liters * gasoline_per_ltr
    if 20 < fuel_liters <= 25:
        discount1 = 0.08 * initial_cost
        cost1 = initial_cost - discount1
    elif fuel_liters > 25 :
        discount1 = 0.1 * initial_cost
        cost1 = initial_cost - discount1
        if club_card == 'Yes' :
            discount2 = 0.18 * fuel_liters
            cost2 = cost1 - discount2
            print(f"{cost2:.2f}")
        else :
            print(f"{cost1:.2f}")


elif fuel_type == 'Gas' :
    initial_cost = fuel_liters * gas_per_ltr
    if 20 < fuel_liters <= 25:
        discount1 = 0.08 * initial_cost
        cost1 = initial_cost - discount1
        if club_card == 'Yes':
            discounted_price = gas_per_ltr -0.08
            cost2 = (fuel_liters * gas_per_ltr)
            if 20 < fuel_liters <= 25:
                discount1 = 0.08 * cost2
                cost3 = cost2 - discount1
                print(f"{cost2:.2f}")
        else :
            print(f"{cost1:.2f}")
    elif fuel_liters > 25:
        discount1 = 0.1 * initial_cost
        cost1 = initial_cost - discount1
        if club_card == 'Yes':
            discounted_price = gas_per_ltr -0.08
            cost2 = fuel_liters * gas_per_ltr
            print(f"{cost2:.2f}")
        else :
            print(f"{cost1:.2f}")


elif fuel_type == 'Diesel' :
    initial_cost = fuel_liters * diesel_per_ltr
    if 20 < fuel_liters <= 25:
        discount1 = 0.08 * initial_cost
        cost1 = initial_cost - discount1
    elif fuel_liters > 25:
        discount1 = 0.1 * initial_cost
        cost1 = initial_cost - discount1
        if club_card == 'Yes':
            discount2 = 0.12 * fuel_liters
            cost2 = cost1 - discount2
            print(f"{cost2:.2f}")
        else:
            print(f"{cost1:.2f}")


