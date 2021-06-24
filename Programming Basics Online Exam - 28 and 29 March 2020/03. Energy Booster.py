fruit = input()
size = input()
count_of_orders = int(input())
watermelon_price = 0
mango_price = 0
pineapple_price = 0
raspberry_price = 0
bill = 0
if size == "small":
    if fruit == "Watermelon":
        watermelon_price = 56 * 2
        bill = watermelon_price * count_of_orders
    elif fruit == "Mango":
        mango_price = 36.66 * 2
        bill = mango_price * count_of_orders
    elif fruit == "Pineapple":
        pineapple_price = 42.10 * 2
        bill = pineapple_price * count_of_orders
    elif fruit == "Raspberry":
        raspberry_price = 20 * 2
        bill = raspberry_price * count_of_orders
elif size == "big":
    if fruit == "Watermelon":
        watermelon_price = 28.70 * 5
        bill = watermelon_price * count_of_orders
    elif fruit == "Mango":
        mango_price = 19.60 * 5
        bill = mango_price * count_of_orders
    elif fruit == "Pineapple":
        pineapple_price = 24.80 * 5
        bill = pineapple_price * count_of_orders
    elif fruit == "Raspberry":
        raspberry_price = 15.20 * 5
        bill = raspberry_price * count_of_orders
if 400 <= bill <= 1000:
    bill = bill - (bill * 0.15)
elif bill > 1000:
    bill /= 2
print(f"{bill:.2f} lv.")