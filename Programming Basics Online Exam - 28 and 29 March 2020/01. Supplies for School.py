pens_count = int(input())
markers_count = int(input())
chemical_for_cleaning_desk_by_liter = float(input())
discount_in_percent = int(input())
discount_in_percent1 = discount_in_percent * 0.01
pens_price = pens_count * 5.80
markers_price = markers_count * 7.20
chemical_price = chemical_for_cleaning_desk_by_liter * 1.20
summary = pens_price + markers_price + chemical_price
summary_with_discount = summary - (summary * discount_in_percent1)
print(f"{summary_with_discount:.3f}")