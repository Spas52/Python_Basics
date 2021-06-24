town = input()
sales = float(input())
if town == "Sofia":
    if 0 <= sales <= 500:
        print(f'{0.05 * sales:.2f}')
    elif 500 < sales <= 1000:
        print(f'{0.07 * sales:.2f}')
    elif 1000 < sales <= 10000:
        print(f'{0.08 * sales:.2f}')
    elif sales > 10000:
        print(f'{0.12 * sales:.2f}')
    else:
        print("error")
elif town == "Varna":
    if 0 <= sales <= 500:
        print(f'{0.045 * sales:.2f}')
    elif 500 < sales <= 1000:
        print(f'{0.075 * sales:.2f}')
    elif 1000 < sales <= 10000:
        print(f'{0.10 * sales:.2f}')
    elif sales > 10000:
        print(f'{0.13 * sales:.2f}')
    else:
        print("error")
elif town == "Plovdiv":
    if 0 <= sales <= 500:
        print(f'{0.055 * sales:.2f}')
    elif 500 < sales <= 1000:
        print(f'{0.08 * sales:.2f}')
    elif 1000 < sales <= 10000:
        print(f'{0.12 * sales:.2f}')
    elif sales > 10000:
        print(f'{0.145 * sales:.2f}')
    else:
        print("error")
else:
    print("error")