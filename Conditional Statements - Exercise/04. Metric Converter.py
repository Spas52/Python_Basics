number = float(input())
a = str(input())
b = str(input())
result = 0
if a == "mm":
    if b == "cm":
        result = number / 10
    elif b == "m":
        result = number / 1000
elif a == "cm":
    if b == "mm":
        result = number * 10
    elif b == "m":
        result = number / 100
elif a == "m":
    if b == "mm":
        result = number * 1000
    elif b == "cm":
        result = number * 100
print(f"{result:.3f}")
