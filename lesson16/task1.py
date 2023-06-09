# Make a class structure in python representing people at school.
# Make a base class called Person, a class called Student, and another one called Teacher.
# Try to find as many methods and attributes as you can which belong to different classes,
# and keep in mind which are common and which are not.
# For example, the name should be a Person attribute, while salary should only be available to the teacher.


class Person():
    def __init__(self, name, lastName, age):
        self.name = name
        self.age = age
        self.lastName = lastName


class Student(Person):
    def __init__(self, name, lastName, age, course, direction):
        super().__init__(name, lastName, age)
        self.course = course
        self.direction = direction


class Teacher(Person):
    def __init__(self, name, age, lastName, classNumber, subject, salary):
        super().__init__(name, lastName, age)
        self.salary = salary
        self.subject = subject
        self.classNumber = classNumber