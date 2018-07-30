students = []


class Student:

    school_name = "SpringField"

    def __init__(self, name, student_id=000):
        self.name = name
        self.student_id = student_id
        students.append(self)

    def __str__(self):
        return "Student " + self.name

    def get_name_captitalize(self):
        return self.name.capitalize()

    def get_school_name(self):
        self.school_name


class HighSchoolStudent(Student):

    school_name = "High School"

    def get_school_name(self):
        return "This is high School"


james = HighSchoolStudent("james")

print(james.get_name_captitalize())
print(james.school_name)