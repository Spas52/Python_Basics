jury = int(input())
command = input()
final_grade = 0
counter_of_examines = 0
while command != "Finish":
    presentation_name = command
    middle_grade = 0
    for grades in range(jury):
        current_grade = float(input())
        middle_grade += current_grade
        counter_of_examines += 1
        final_grade += current_grade
    middle_grade /= jury
    print(f"{presentation_name} - {middle_grade:.2f}.")
    command = input()
final_grade /= counter_of_examines
print(f"Student's final assessment is {final_grade:.2f}.")