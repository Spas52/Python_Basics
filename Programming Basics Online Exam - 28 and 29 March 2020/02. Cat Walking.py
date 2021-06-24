steps_per_day_in_minutes = int(input())
walks_count_on_day = int(input())
cat_calories_per_Day = int(input())
for_every_minute_cat_degrees_calories = 5
summary_of_minutes_for_walks = walks_count_on_day * steps_per_day_in_minutes
summary_of_calories_for_one_day = summary_of_minutes_for_walks * for_every_minute_cat_degrees_calories
cat_calories_per_Day_devided = cat_calories_per_Day / 2
if summary_of_calories_for_one_day >= cat_calories_per_Day_devided:
    print(f"Yes, the walk for your cat is enough. Burned calories per day: {summary_of_calories_for_one_day}.")
else:
    print(f"No, the walk for your cat is not enough. Burned calories per day: {summary_of_calories_for_one_day}.")