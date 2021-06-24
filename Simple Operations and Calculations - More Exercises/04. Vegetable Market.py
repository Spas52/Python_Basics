kg_for_vegetables = float(input())
kg_for_fruits = float(input())
sum_for_vegetables = int(input())
sum_for_fruits = int(input())
end_v = kg_for_vegetables * sum_for_vegetables
end_f = kg_for_fruits * sum_for_fruits
summary = (end_f + end_v) / 1.94
print(f"{summary:.2f}")