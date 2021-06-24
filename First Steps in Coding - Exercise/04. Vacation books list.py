# Брой страници в текущата книга - цяло число
# Страници, които може да прочита за 1 час - цяло число
# Броя на дните, за които трябва да прочете книгата - цяло число
number_of_pages = int(input())
pages_per_hour = int(input())
number_of_days = int(input())
hours_per_day = (number_of_pages / pages_per_hour) / number_of_days
print(hours_per_day)

