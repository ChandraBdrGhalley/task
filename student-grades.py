num_students = int(input("Enter the number of students: "))

i = 1
while i <= num_students:
    total_grade = 0
    num_subjects = int(input(f"Enter the number of subjects for the student {i}"))

    for j in range(1, num_students + 1):
        grade = float(input(f"Enter subject {j} grade for student {}: "))
        total_grade += grade

    average_grade = total_grade / num_subjects
    print(f"Average grade for student {i}: {average: 2f}")
    i += 1

