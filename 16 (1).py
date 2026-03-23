class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, roll, marks):
        super().__init__(name)
        self.roll = roll
        self.marks = marks

    def display(self):
        print(f"Student: {self.name}, Roll: {self.roll}, Marks: {self.marks}")

class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

    def display(self):
        print(f"Teacher: {self.name}, Subject: {self.subject}")

class Admin(Person):
    def __init__(self, name, department):
        super().__init__(name)
        self.department = department

    def display(self):
        print(f"Admin: {self.name}, Department: {self.department}")

s = Student("Rahul", 1, 90)
t = Teacher("Aman Sir", "Maths")
a = Admin("Neha", "Exams")

s.display()
t.display()
a.display()
