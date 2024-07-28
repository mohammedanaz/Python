from datetime import datetime

list_of_tuples = [
    (1, 'apple'),
    (2, 'banana'),
    (3, 'cherry'),
    (4, 'date'),
    (5, 'elderberry')
]

my_dict = dict.fromkeys(list_of_tuples)
my_dict.setdefault(6, 'default')
print(len(list_of_tuples), len(my_dict))

def add(x, y):
    print(x + y)

def add(x, y, z):
    print(x + y + z)

add(1, 2, 3)



class MyClass():
    __cls_var = 'i am class var'

    def __new__(cls, *args, **kwargs):
        print('new method called')
        return super(MyClass, cls).__new__(cls)

    current_year = datetime.now().year
    def __init__(self, name, age) -> None:
        print('init method called')
        self.name = name
        self.age = age

    def __len__(self):
        return 10

    def greet(self):
        print(f'hi {self.name}. you are {self.age} years old.')

    @classmethod
    def create_obj(cls, name, year):
        age = cls.current_year - year
        return cls(name, age)


obj1 = MyClass.create_obj('adam', 1990)
obj1.greet()

print(len(obj1))
