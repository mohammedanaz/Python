my_list = [2,5,4,7,9,7,55,4,22,66,7,8,9]
# my_list.sort()
# print(my_list)

for x in range(len(my_list)):
    for y in range(x+1,len(my_list)):
        if my_list[x] > my_list[y]:
            temp = my_list[x]
            my_list[x] = my_list[y]
            my_list[y] = temp

print(my_list)