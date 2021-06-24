trunk = float(input())

counter = 0

while True:
    line = input()

    if line == 'End':
        print(f'Congratulations! All suitcases are loaded!\nStatistic: {counter} suitcases loaded.')
        break

    suitcase = float(line)
    if (counter + 1) % 3 == 0:
        suitcase *= 1.1

    if suitcase > trunk:
        print(f'No more space!\nStatistic: {counter} suitcases loaded.')
        break

    trunk -= suitcase
    counter += 1