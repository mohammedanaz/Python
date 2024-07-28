from datetime import datetime

list_of_tuples = [
    (1, 'apple'),
    (2, 'banana'),
    (3, 'cherry'),
    (4, 'date'),
    (5, 'elderberry')
]

class MyClass():
    __cls_var = 'i am class var'
    current_year = datetime.now().year
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def greet(self):
        print(f'hi {self.name}. you are {self.age} years old.')

    @classmethod
    def create_obj(cls, name, year):
        age = cls.current_year - year
        return cls(name, age)


obj1 = MyClass.create_obj('adam', 1990)
obj1.greet()
