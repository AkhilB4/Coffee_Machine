class Student:

    def __init__(self, name, last_name, birth_year):
        self.name = name
        self.last_name = last_name
        self.birth_year = birth_year
        self.student_id = self.name[0] + self.last_name + str(self.birth_year)


student_name = input()
student_last_name = input()
student_birth_year = int(input())
s = Student(student_name, student_last_name, student_birth_year)
print(s.student_id)
