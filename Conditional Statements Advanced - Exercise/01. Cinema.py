type_of_projection = input()
r = int(input())
c = int(input())
income = 0
cinema_capacity = r * c
if type_of_projection == "Premiere":
    income = cinema_capacity * 12.00
elif type_of_projection == "Normal":
    income = cinema_capacity * 7.50
elif type_of_projection == "Discount":
    income = cinema_capacity * 5.00
print(f"{income:.2f}")
