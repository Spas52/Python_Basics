working_days_for_company = int(input())
number_of_chefs = int(input())
number_of_cakes = int(input())
number_of_waffle = int(input())
number_of_pancakes = int(input())
cake = 45
waffle = 5.8
pancake = 3.2
cakes_money = number_of_cakes * cake
waffles_money = number_of_waffle * waffle
pancakes_money = number_of_pancakes * pancake
summary_for_one_day = (cakes_money + waffles_money + pancakes_money) * number_of_chefs
company_summary = summary_for_one_day * working_days_for_company
summary_after_fees = company_summary - (company_summary / 8)
print(summary_after_fees)

