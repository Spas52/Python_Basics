movie_budget = float(input())
workers = int(input())
price_for_outfit_of_one_worker = float(input())
decoration = movie_budget * 0.1
if workers > 150:
    money_for_outfit = workers * price_for_outfit_of_one_worker - (workers * (price_for_outfit_of_one_worker * 0.1))
else:
    workers <= 150
    money_for_outfit = workers * price_for_outfit_of_one_worker
summary = decoration + money_for_outfit
money_left = movie_budget - summary
if summary > movie_budget:
    print("Not enough money!")
    print(f"Wingard needs {(-1) * money_left:.2f} leva more.")
else:
    summary <= movie_budget
    print("Action!")
    print(f"Wingard starts filming with {money_left:.2f} leva left.")