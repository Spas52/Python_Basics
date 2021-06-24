record = float(input())
distance = float(input())
time_for_swim = float(input())
distance_in_seconds = distance * time_for_swim
interrupt_by_water = (distance // 15) * 12.5
all_time = distance_in_seconds + interrupt_by_water
if record <= all_time:
    time_failed = all_time - record
    print(f"No, he failed! He was {time_failed:.2f} seconds slower.")
else:
    record > all_time
    print(f"Yes, he succeeded! The new world record is {all_time:.2f} seconds.")