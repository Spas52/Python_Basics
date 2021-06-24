deposit_sum = float(input())
deposit_delay = int(input())
year = float(input())
summary = deposit_sum + deposit_delay * ((deposit_sum * year / 100)/12)
print(summary)


