import sys
numbers = int(input())
sum_of_all_numbers = 0
max_element = - sys.maxsize
for number in range(1, numbers + 1):
    new_number = int(input())
    sum_of_all_numbers += new_number
    if new_number > max_element:
        max_element = new_number
if max_element == sum_of_all_numbers - max_element:
    print("Yes")
    print(f"Sum = {max_element}")
else:
    print("No")
    print(f"Diff = {abs(max_element - (sum_of_all_numbers - max_element))}")