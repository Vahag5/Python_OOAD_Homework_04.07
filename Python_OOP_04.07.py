class Student:
    def __init__(self, name, age, student_id):
        self._name = name
        self._age = age
        self.__student_id = student_id  

    def set_name(self, name):
        self._name = name

    def get_name(self):
        return self._name

    def set_age(self, age):
        self._age = age

    def get_age(self):
        return self._age

    def get_student_id(self):
        return self.__student_id  

student = Student("James", 23, "12.56.788.514")

print(f"Name: {student.get_name()}")                   # Name: James
print(f"Age: {student.get_age()}")                     # Age: 23
print(f"Student ID: {student.get_student_id()}")       # Student ID: 12.56.788.514
