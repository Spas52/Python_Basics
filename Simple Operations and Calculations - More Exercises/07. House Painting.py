x = float(input())
y = float(input())
h = float(input())
back_wall = x * x
front_wall = x * x - (1.2 * 2)
side_walls = (x * y - (1.5 * 1.5)) * 2
sum_walls = back_wall + front_wall + side_walls
green_paint = sum_walls / 3.4
roof_sides = (x * y) * 2
roof_back_and_front = (x * h / 2) * 2
sum_roof = roof_sides + roof_back_and_front
red_paint = sum_roof / 4.3
print(f"{green_paint:.2f}")
print(f"{red_paint:.2f}")
