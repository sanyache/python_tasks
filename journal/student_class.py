import json


# noinspection PyArgumentList
def create_json(student_list):
    with open("students.json", "w", encoding='utf-8'):
        json.dump(student_list, default=vars, ensure_ascii=False, indent=4)

subjects = ['математика', "інформатика", "фізика", "хімія"]

class Student:
    def __init__(self, student_id, first_name, last_name, birthday):
        self.id = student_id
        self.first_name = first_name
        self.last_name = last_name
        self.birthday = birthday
        self.subjects = dict()
        for subject in subjects:
             self.subjects[subject] = []

    def add_score(self, subj, score):
        self.subjects[subj].append(score)

    def __str__(self):
        return '{} {}'.format(self.last_name, self.first_name)

students = []
n = int(input("Enter number of students "))
for i in range(n):
    s_first_name = input("Enter first name ")
    s_last_name = input("Enter last name ")
    s_birth = input("Enter birthday ")
    student = Student(i, s_first_name, s_last_name, s_birth)
    print(student)
    students.append(student)

# students[0].add_score(subjects[0],10)
# print(students[0].subjects)

create_json(students)
