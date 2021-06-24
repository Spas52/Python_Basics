dog_food_in_kg = int(input())
command = input()
dog_food_in_gr = dog_food_in_kg * 1000
eaten_food = 0
while command != "Adopted":
    dog_eat = int(command)
    eaten_food += dog_eat
    command = input()
dog_food_in_gr -= eaten_food
if dog_food_in_gr >= 0:
    print(f"Food is enough! Leftovers: {dog_food_in_gr} grams.")
elif dog_food_in_gr < 0:
    print(f"Food is not enough. You need {abs(dog_food_in_gr)} grams more.")