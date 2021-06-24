import math
geometric_figure = str(input())
if geometric_figure == "square":  # S = a.a
    a = float(input())
    area_square = math.pow(a, 2)
    print(f"{area_square:.3f}")
elif geometric_figure == "rectangle":  # S = a * b
    a = float(input())
    b = float(input())
    area_rectangle = a * b
    print(f"{area_rectangle:.3f}")
elif geometric_figure == "circle":  # S = pi * r * r
    radius = float(input())
    area_circle = math.pi * math.pow(radius, 2)
    print(f"{area_circle:.3f}")
elif geometric_figure == "triangle":  # S = (a * h) / 2
    a = float(input())
    h = float(input())
    area_triangle = (a * h) / 2
    print(f"{area_triangle:.3f}")
