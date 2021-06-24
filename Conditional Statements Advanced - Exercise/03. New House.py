flower_type = input()
flower_count = int(input())
money = int(input())
roses = 5
dahlias = 3.80
tulips = 2.80
narcissus = 3
gladiolus = 2.50
price = 0
if flower_type == "Roses":
    price = roses * flower_count
    if flower_count > 80:
        price = price - (price * 0.1)
elif flower_type == "Dahlias":
    price = dahlias * flower_count
    if flower_count > 90:
        price = price - (price * 0.15)
elif flower_type == "Tulips":
    price = tulips * flower_count
    if flower_count > 80:
        price = price - (price * 0.15)
elif flower_type == "Narcissus":
    price = narcissus * flower_count
    if flower_count < 120:
        price = price + (price * 0.15)
elif flower_type == "Gladiolus":
    price = gladiolus * flower_count
    if flower_count < 80:
        price = price + (price * 0.2)
if money >= price:
    left_money = money - price
    print(f"Hey, you have a great garden with {flower_count} {flower_type} and {left_money:.2f} leva left.")
else:
    need = price - money
    print(f"Not enough money, you need {need:.2f} leva more.")
