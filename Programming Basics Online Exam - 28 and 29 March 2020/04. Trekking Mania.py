groups_of_climbing = int(input())
peak = ""
all_people = 0
musala_people = 0
monblan_people = 0
kilimandjaro_people = 0
k2_people = 0
everest_people = 0
for group in range(1, groups_of_climbing + 1):
    people = int(input())
    if people <= 5:
        peak = "Musala"
        musala_people += people
    elif 6 <= people <= 12:
        peak = "Monblan"
        monblan_people += people
    elif 13 <= people <= 25:
        peak = "Kilimandjaro"
        kilimandjaro_people += people
    elif 26 <= people <= 40:
        peak = "K2"
        k2_people += people
    elif people >= 41:
        peak = "Everest"
        everest_people += people
    all_people += people
musala_people_in_percent = musala_people / all_people * 100
monblan_people_in_percent = monblan_people / all_people * 100
kilimandjaro_people_in_percent = kilimandjaro_people / all_people * 100
k2_people_in_percent = k2_people / all_people * 100
everest_people_in_percent = everest_people / all_people * 100
print(f"{musala_people_in_percent:.2f}%")
print(f"{monblan_people_in_percent:.2f}%")
print(f"{kilimandjaro_people_in_percent:.2f}%")
print(f"{k2_people_in_percent:.2f}%")
print(f"{everest_people_in_percent:.2f}%")
