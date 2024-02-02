n = int(input("Enter the limit value: "))

my_list = [0,1]

for i in range(2, n):
    my_list.append(my_list[-1] + my_list[-2])
print(my_list)