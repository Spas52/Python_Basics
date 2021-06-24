money_needed = float(input())
money_in_hand = float(input())
command = ""
summ_that_will_spend = 0
spending_days = 0
total_days = 0
while True:
    action = input()
    current_sum = float(input())
    total_days += 1
    if action == "spend":
        money_in_hand -= current_sum
        if money_in_hand < 0:
            money_in_hand = 0
        spending_days += 1
        if spending_days == 5:
            break
    elif action == "save":
        money_in_hand += current_sum
        if money_in_hand >= money_needed:
            break
        spending_days = 0
if money_in_hand >= money_needed:
    print(f"You saved the money for {total_days} days.")
else:
    print(f"You can't save the money.")
    print(f"{total_days}")