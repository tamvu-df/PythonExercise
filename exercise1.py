from statistics import mean

num_students = 5
student_dict = {}
for i in range(num_students):
    student_info = input(
        f"Input student number {i+1} name and their corresponding grade, separated by comma: "
    )
    student_info_list = student_info.split(",")
    student_name = student_info_list[0].strip()
    student_grade = float(student_info_list[1].strip())
    student_dict[f"{student_name}"] = student_grade

max_grade = max(student_dict.items(), key=lambda x: x[1])
print(f"Max Grade:{max_grade}")

min_grade = min(student_dict.items(), key=lambda x: x[1])
print(f"Min Grade:{min_grade}")

average_grade = mean(student_dict.values())
print(f"Average Grade:{average_grade}")

student_dict = {
    f"{name}": grade
    for name, grade in sorted(student_dict.items(), key=lambda x: x[1], reverse=True)
}
print(f"Student dictionary, sorted descending: {student_dict}")

student_dict = {
    f"{name}": grade for name, grade in sorted(student_dict.items(), key=lambda x: x[1])
}
print(f"Student dictionary, sorted ascending: {student_dict}")
