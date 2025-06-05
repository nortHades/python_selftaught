class Student:
    def __init__(self, name, age, grade):
        # Instance attr
        self.name = name
        self.age = age
        self.grade = grade

    def introduce(self):
        return f"Hi, I'm {self.name}, {self.age} years old, grade {self.grade}"
