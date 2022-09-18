from math import floor
number_of_planned_processors = int(input())
workers = int(input())
work_days = int(input())
processor_price = 110.10
total_work_hours = (8 * work_days) * workers
processors_made = total_work_hours / 3
processors_made = floor(processors_made)
money_made = processors_made * processor_price
diff = abs((number_of_planned_processors - processors_made) * processor_price)
if processors_made >= number_of_planned_processors:
    print(f"Profit: -> {diff:.2f} BGN")
else:

    print(f"Losses: -> {diff:.2f} BGN")
