month = input()
number_of_nights = int(input())
studio = 0
apartment = 0
if month == "May" or month == "October":
    studio = 50
    apartment = 65
    if 7 < number_of_nights <= 14:
        studio = studio - (studio * 0.05)
    elif number_of_nights > 14:
        studio = studio - (studio * 0.3)
        apartment = apartment - (apartment * 0.1)
elif month == "June" or month == "September":
    studio = 75.20
    apartment = 68.70
    if number_of_nights > 14:
        studio = studio - (studio * 0.2)
        apartment = apartment - (apartment * 0.1)
elif month == "July" or month == "August":
    studio = 76
    apartment = 77
    if number_of_nights > 14:
        apartment = apartment - (apartment * 0.1)
price_studio = studio * number_of_nights
price_apartment = apartment * number_of_nights
print(f"Apartment: {price_apartment:.2f} lv.")
print(f"Studio: {price_studio:.2f} lv.")