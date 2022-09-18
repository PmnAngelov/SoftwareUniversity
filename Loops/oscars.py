actor = input()
academy_points = float(input())
number_of_scorers = int(input())
for num in range(number_of_scorers):
    name_of_scorer = input()
    points_given = float(input())
    actual_points_given = len(name_of_scorer) * points_given / 2
    academy_points += actual_points_given
    if academy_points > 1250.5:
        break

if academy_points > 1250.5:
    print(f"Congratulations, {actor} got a nominee for leading role with {academy_points:.1f}!")
else:
    diff = 1205.5 - academy_points
    print(f"Sorry, {actor} you need {diff:.1f} more!")


