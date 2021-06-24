money = float(input())
gender = input()
age = int(input())
sport = input()
if gender == "m":
    if sport == "Gym":
        card = 42
    elif sport == "Boxing":
        card = 41
    elif sport == "Yoga":
        card = 45
    elif sport == "Zumba":
        card = 34
    elif sport == "Dances":
        card = 51
    elif sport == "Pilates":
        card = 39
elif gender == "f":
    if sport == "Gym":
        card = 35
    elif sport == "Boxing":
        card = 37
    elif sport == "Yoga":
        card = 42
    elif sport == "Zumba":
        carda = 31
    elif sport == "Dances":
        card = 53
    elif sport == "Pilates":
        card = 37
if age <= 19:
    card *= 0.8
summary = abs(money - card)
if money >= card:
    print(f"You purchased a 1 month pass for {sport}.")
else:
    print(f"You don't have enough money! You need ${summary:.2f} more.")