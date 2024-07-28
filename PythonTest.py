list_of_tuples = [
    (1, 'apple'),
    (2, 'banana'),
    (3, 'cherry'),
    (4, 'date'),
    (5, 'elderberry')
]

class MyClass():
    __cls_var = 'i am class var'

    def __init__(self, msg):
        self.msg = msg

    def call_var(self):
        print(f'class var is {self.__cls_var}')

obj1 = MyClass('msg1')
print(obj1.__cls_var)
