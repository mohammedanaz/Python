my_list_1 = [1,2,3,4,5]
my_list_2 = [4,5,6,7,8,9]

union_list = my_list_1 + [item for item in my_list_2 if item not in my_list_1]

print(union_list)