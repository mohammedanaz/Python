n = int(input("Enter the limit value: "))

my_list = [0,1]

for i in range(2, n):
    my_list.append(my_list[-1] + my_list[-2])
print(my_list)


# another method memory effient

# def my_gen(n):   
#     a, b = 0, 1
#     yield a
#     for i in range(n-1):
#         yield b
#         a, b = b, a + b

# for num in my_gen(5):
#     print(num, end=' ')