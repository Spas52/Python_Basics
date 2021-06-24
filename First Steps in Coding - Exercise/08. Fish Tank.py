long = int(input())
wide = int(input())
high = int(input())
occupied_volume = float(input())
volume_of_fish_tank = long * wide * high
liters_that_can_handle = volume_of_fish_tank * 0.001
percent = occupied_volume * 0.01
liters_that_will_need = liters_that_can_handle * (1 - percent)
print(liters_that_will_need)

