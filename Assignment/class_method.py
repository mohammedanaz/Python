from datetime import datetime

class MyClass:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f'Hi {self.name}. You are {self.age} years old.')

    @classmethod
    def create_obj(cls, name, year):
        current_year = datetime.now().year
        age = current_year - year
        return cls(name, age)
    

obj1 = MyClass('Adam', 30)

obj1.greet()

obj2 = MyClass.create_obj('Adam', 1990)
obj2.greet()