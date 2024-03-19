class MyExpt(Exception):
    def __init__(self):
        print('My exception occurred')

try:
    1/0
except ZeroDivisionError:
    try:
        raise MyExpt()
    except MyExpt as e:
        print(str(e))
