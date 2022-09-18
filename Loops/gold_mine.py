number_of_locations = int(input())

for locations in range(number_of_locations):
    expected_average_gold_for_the_day = float(input())
    days_digging = int(input())
    total_gold = 0
    for days in range(days_digging):
        actual_gold_mined = float(input())
        total_gold += actual_gold_mined
    average_gold_for_the_location = total_gold / days_digging
    if average_gold_for_the_location >= expected_average_gold_for_the_day:
        print(f"Good job! Average gold per day: {average_gold_for_the_location:.2f}.")
    else:
        diff = expected_average_gold_for_the_day - average_gold_for_the_location
        print(f"You need {diff:.2f} gold.")


