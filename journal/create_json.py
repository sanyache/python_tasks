import json
n = input("Enter number of student = ")
students = []
subjects = ["алгебра", "англійська", "інформатика", "фізика"]
for i in range(int(n)):
    student = dict()
    student['id'] = i
    student['first_name'] = input("Enter first name ")
    student['last_name'] = input("Enter last name ")
    student['birthday'] = input("Enter birthday ")
    for subject in subjects:
        student[subject] = []
    students.append(student)
with open("data.json", "w", encoding='utf-8') as file:
    json.dump(students, file, ensure_ascii=False, indent=4)
print(students)
