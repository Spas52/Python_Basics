strawberries_price_for_kg = float(input())
banana_count = float(input())
oranges_count = float(input())
raspberries_count = float(input())
strawberries_count = float(input())
raspberries_price = strawberries_price_for_kg / 2
oranges_price_for_kg = raspberries_price - (0.4 * raspberries_price)
bananas_price_for_kg = raspberries_price - (0.8 * raspberries_price)
summary_for_raspberries = raspberries_count * raspberries_price
summary_for_oranges = oranges_count * oranges_price_for_kg
summary_for_bananas = banana_count * bananas_price_for_kg
summary_for_strawberries = strawberries_count * strawberries_price_for_kg
big_summary = summary_for_raspberries + summary_for_oranges + summary_for_bananas + summary_for_strawberries
print(big_summary)




