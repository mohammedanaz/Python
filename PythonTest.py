
student_dicts = [
    {'name': 'Adam', 'class': 1, 'mark': 40},
    {'name': 'Eve', 'class': 2, 'mark': 50},
    {'name': 'John', 'class': 3, 'mark': 60},
]

highest_mark = {'result': {'mark':-1}}

def find_highest_mark(lst):

    for obj in lst:
        if highest_mark['result']['mark'] < obj['mark']:
            highest_mark['result'] = obj
    print(highest_mark['result'])

find_highest_mark(student_dicts)