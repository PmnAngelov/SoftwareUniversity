import sys

number_of_balls = int(input())
maxa = -sys.maxsize
perfect_weight = 0
perfect_time = 0
perfect_quality = 0

for ball in range(number_of_balls):
    weight = int(input())
    time_needed = int(input())
    quality = int(input())
    score = (weight / time_needed) ** quality
    if score > maxa:
        maxa = score
        perfect_weight = weight
        perfect_quality = quality
        perfect_time = time_needed

print(f"{perfect_weight} : {perfect_time} = {int(maxa)} ({perfect_quality})")