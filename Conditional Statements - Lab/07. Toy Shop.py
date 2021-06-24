price = float(input())
puzzels = int(input())
dolls = int(input())
teddy_bears = int(input())
miners = int(input())
tracks = int(input())

sum = puzzels * 2.6 + dolls * 3 + teddy_bears * 4.1 + miners * 8.2 + tracks * 2
toys = puzzels + dolls + teddy_bears + miners + tracks

if toys >= 50:
    sum = sum - sum * 0.25

rent = sum * 0.1
sum = sum - rent

if sum >= price:
    diff = sum - price
    print(f'Yes! {diff:.2f} lv left.')
else:
    diff = price - sum
    print(f' Not enough money! {diff:.2f} lv needed.')