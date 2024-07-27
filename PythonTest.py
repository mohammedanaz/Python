list_of_tuples = [
    (1, 'apple'),
    (2, 'banana'),
    (3, 'cherry'),
    (4, 'date'),
    (5, 'elderberry')
]
my_dict = {k: v.upper() for k,v in list_of_tuples}

print(my_dict)