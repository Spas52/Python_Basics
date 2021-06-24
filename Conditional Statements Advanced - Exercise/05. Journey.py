budget = float(input())
season = input()
destination = ""
place = ""
price = 0
if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        place = "Camp"
        price = budget - (budget * 0.7)
    elif season == "winter":
        place = "Hotel"
        price = budget - (budget * 0.3)
elif budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        place = "Camp"
        price = budget - (budget * 0.6)
    elif season == "winter":
        place = "Hotel"
        price = budget - (budget * 0.2)
elif budget > 1000:
    destination = "Europe"
    place = "Hotel"
    if season == "summer" or season == "winter":
        price = budget - (budget * 0.1)
print(f"Somewhere in {destination}")
print(f"{place} - {price:.2f}")