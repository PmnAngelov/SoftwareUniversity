kilometers = int(input())
time_of_day = str(input())
taxi_starting_tax = 0.70
taxi_day_tax = 0.79
taxi_night_tax = 0.90
bus_tax_day_or_night = 0.09   #minimum 20 km
train_tax_day_or_night = 0.06   #minimum 100 km
if kilometers < 20:
    if time_of_day == 'day':
        total_tax = taxi_starting_tax + kilometers * taxi_day_tax
        print(f"{total_tax:.2f}")
    elif time_of_day == 'night':
        total_tax = taxi_starting_tax + kilometers * taxi_night_tax
        print(f"{total_tax:.2f}")
if 20 <= kilometers < 100 :
    if time_of_day == 'day':
        total_tax = bus_tax_day_or_night * kilometers
        print(f"{total_tax:.2f}")
    elif time_of_day == 'night':
        total_tax = bus_tax_day_or_night * kilometers
        print(f"{total_tax:.2f}")
if kilometers >= 100 :
    if time_of_day == 'day':
        total_tax = train_tax_day_or_night * kilometers
        print(f"{total_tax:.2f}")
    elif time_of_day == 'night':
        total_tax = train_tax_day_or_night * kilometers
        print(f"{total_tax:.2f}")