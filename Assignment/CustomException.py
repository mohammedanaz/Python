class MyError(Exception):
    def __init__(self,msg):
        self.msg = msg


def my_fn(a,b):
    str_len = len(str(a + b))
    if str_len > 2:
        raise MyError("Error - Bigger sum")
    else:
        print(f'The sum is - {a + b}')

try:
    my_fn(2,100)
except MyError as e:
    print(f'{e}')