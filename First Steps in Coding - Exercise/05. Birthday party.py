# Наем на залата
# Торта - цената й е 20% от наема на залата
# Напитки - цената им е 45% по-малко от тази на тортата
# Аниматор цената му е 1/3 от цената за наема на залата
room_rent = int(input())
cake = room_rent * (20 / 100)
drinks = cake * 0.55
animator = room_rent / 3
summary = room_rent + cake + drinks + animator
print(summary)



