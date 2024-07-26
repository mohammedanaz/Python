
class MyException(Exception):
    
    def __init__(self, msg):
        self.msg = f'My Exception Caught: {msg}'

def my_fn(a, b):

    if a/b < 1:
        raise MyException('Divisor cant be less than dividend')
    
    return a/b
try:
    print(my_fn(2, 3))
except MyException as e:
    print(str(e))

x = 2

print(x)