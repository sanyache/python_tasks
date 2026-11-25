n = int(input("Enter number of student = "))
students = []
for _ in range(n):
    student = dict()
    student['first_name'] = input("Enter first name ")
    student['last_name'] = input("Enter last name ")
    student['score'] = int(input("Enter students score "))
    students.append(student)
students.sort(key=lambda x: x['score'])
print(students)