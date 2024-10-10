def add_score(subj, id_stud, score):
     f_student = next((item for item in students if item["id"] == id_stud), None)
     print(f_student[subj].append(score))

n = input("Enter number of student = ")
students = []
subjects = [sub for sub in input("Enter subjects ").split()]
for i in range(int(n)):
    student = dict()
    student['id'] = i
    student['first_name'] = input("Enter first name ")
    student['last_name'] = input("Enter last name ")
    student['birthday'] = input("Enter birthday ")
    for subject in subjects:
        student[subject] = []
    students.append(student)
add_score('math', 1, 12)
print(students)
