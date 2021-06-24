# room_for_one_person = 18.00
# apartment = 25.00
# president_apartment = 35.00
days = int(input())
room_type = input()
grade = input()
final_price = 0
nights = days - 1
if room_type == "room for one person":
    final_price = nights * 18
elif room_type == "apartment":
    final_price = nights * 25
elif room_type == "president apartment":
    final_price = nights * 35
if room_type == "apartment":
    if days < 10:
        final_price = final_price - (0.30 * final_price)
    elif 10 <= days <= 15:
        final_price = final_price - (0.35 * final_price)
    elif days > 15:
        final_price = final_price - (0.50 * final_price)
if room_type == "president apartment":
    if days < 10:
        final_price = final_price - (0.10 * final_price)
    elif 10 <= days <= 15:
        final_price = final_price - (0.15 * final_price)
    elif days > 15:
        final_price = final_price - (0.20 * final_price)
if grade == "positive":
    final_price = final_price + (0.25 * final_price)
elif grade == "negative":
    final_price = final_price - (0.10 * final_price)

print(f"{final_price:.2f}")





