age = int(input())
laundry_price = float(input())
toy_price = int(input())

money = 0
for i in range(1, age + 1):
    if i % 2 == 0:
        money += i * 5 - 1

    else:
        money += toy_price

result = abs(money - laundry_price)
if money < laundry_price:
    print(f"No! {result:.2f}")
else:
    print(f"Yes! {result:.2f}")