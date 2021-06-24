hour_of_examine = int(input())
minute_of_examine = int(input())
hour_of_arriving = int(input())
minute_of_arriving = int(input())
time_of_examine_in_minutes = hour_of_examine * 60 + minute_of_examine
time_of_arriving_in_minutes = hour_of_arriving * 60 + minute_of_arriving
difference = abs(time_of_examine_in_minutes - time_of_arriving_in_minutes)
if time_of_arriving_in_minutes > time_of_examine_in_minutes:
    print("Late")
elif time_of_examine_in_minutes - 30 <= time_of_arriving_in_minutes <= time_of_examine_in_minutes:
    print("On time")
elif time_of_arriving_in_minutes < time_of_examine_in_minutes - 30:
    print("Early")
if time_of_examine_in_minutes - 60 < time_of_arriving_in_minutes < time_of_examine_in_minutes:
    print(f"{difference} minutes before the start")
elif time_of_arriving_in_minutes <= time_of_examine_in_minutes - 60:
    hours = difference // 60
    minutes = difference % 60
    if minutes <= 9:
        print(f"{hours}:0{minutes} hours before the start")
    else:
        print(f"{hours}:{minutes} hours before the start")
elif time_of_examine_in_minutes < time_of_arriving_in_minutes < time_of_examine_in_minutes + 60:
    print(f"{difference} minutes after the start")
elif time_of_arriving_in_minutes >= time_of_examine_in_minutes + 60:
    hours = difference // 60
    minutes = difference % 60
    if minutes <= 9:
        print(f"{hours}:0{minutes} hours after the start")
    else:
        print(f"{hours}:{minutes} hours after the start")