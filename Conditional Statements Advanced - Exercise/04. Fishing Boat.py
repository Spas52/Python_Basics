budget_of_the_group = int(input())
season = input()
fisher_man = int(input())
price = 0
if season == "Spring":
    price = 3000
elif season == "Summer" or season == "Autumn":
    price = 4200
elif season == "Winter":
    price = 2600
if fisher_man <= 6:
    price *= 0.9
elif 7 <= fisher_man <= 11:
    price *= 0.85
elif fisher_man >= 12:
    price *= 0.75
if fisher_man % 2 == 0 and season != "Autumn":
    price *= 0.95
difference = abs(budget_of_the_group - price)
if budget_of_the_group >= price:
    print(f"Yes! You have {difference:.2f} leva left.")
else:
    print(f"Not enough money! You need {difference:.2f} leva.")