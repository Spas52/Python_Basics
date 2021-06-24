w = float(input())
h = float(input())
w_in_cm = w * 100
h_in_cm = h * 100
h_without_corridor = h_in_cm - 100
bura_na_red = int(h_without_corridor / 70)
kolko_reda = int(w_in_cm / 120)
how_many_seats = bura_na_red * kolko_reda - 3
print(f"{how_many_seats:.0f}")