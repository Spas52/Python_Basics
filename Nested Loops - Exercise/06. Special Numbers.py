number = int(input())
for numbers in range(1111, 9999):
    is_Magic = True
    number_as_string = str(numbers)
    for digit in number_as_string:
        if int(digit) == 0 or number % int(digit) != 0:
            is_Magic = False
            break
    if is_Magic:
        print(f"{number_as_string}", end=" ")
