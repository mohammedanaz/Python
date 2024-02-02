my_list = [1,2,2,3,4,4,5,6,7,8,8,8,9]

new_list = []

for x in my_list:
    if x not in new_list:
        new_list.append(x)

print(new_list)