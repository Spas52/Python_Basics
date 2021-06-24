import math
record_in_seconds = float(input())
distance_in_metres = float(input())
time_in_second_for_climbing_one_meter = float(input())
slow_in_seconds = (math.floor(distance_in_metres / 50)) * 30
time_for_climbing = (distance_in_metres * time_in_second_for_climbing_one_meter) + slow_in_seconds
difference = abs(time_for_climbing - record_in_seconds)
if time_for_climbing < record_in_seconds:
    print(f"Yes! The new record is {time_for_climbing:.2f} seconds.")
else:
    print(f"No! He was {difference:.2f} seconds slower.")

