students = []



def get_students_titlecase():
    students_titlecase = []
    for student in students:
        students_titlecase.append(student["name"].title())

    return students_titlecase


# def print_students_titlecase():
#     students_titlecase = []
#     for student in students:
#         students_titlecase = student.title()
#
#     print(students_titlecase)

def print_students_titlecase():
    students_titlecase = get_students_titlecase()

    print(students_titlecase)


def add_student(name, student_id=1):
    student = {"name": name, "student_id": student_id}
    students.append(student)


#
# def var_args(name, *args):
#     print(name)
#     print(args)



# var_args("mark", "Loves Python", None, "Hello")



def save_file(student):
    try:
        f = open("students.txt", "a")
        f.write(student + "\n")
        f.close()
    except Exception:
        print("could not save file")

def read_file():
    try:
        f = open("students.txt", "r")
        for student in f.readlines():
            add_student(student)
        f.close()
    except Exception:
        print("could not read file")

read_file()
print_students_titlecase()

# while True:
#     choice = input("DO you want to continue (Yes or No)")
#     if choice in ('no', 'No', 'NO'):
#         break
#
#     student_name = input("Enter student name")
#     student_id = input("ENter student id")
#
#     add_student(student_name, student_id)

student_name = input("Enter student name")
student_id = input("Enter student ID")

save_file(student_name)

print("Completing Entry")
print_students_titlecase()
