sum = float(input())
counter_of_coins = 0
sum = int(sum * 100)
while sum > 1:
     counter_of_coins += sum // 200
     sum = sum % 200
     counter_of_coins += sum // 100
     sum = sum % 100
     counter_of_coins += sum // 50
     sum = sum % 50
     counter_of_coins += sum // 20
     sum = sum % 20
     counter_of_coins += sum // 10
     sum = sum % 10
     counter_of_coins += sum // 5
     sum = sum % 5
     counter_of_coins += sum // 2
     sum = sum % 2
     if sum == 1:
         counter_of_coins += 1
         break
print(f"{counter_of_coins:.0f}")