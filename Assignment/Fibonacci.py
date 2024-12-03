# n = int(input("Enter the limit value: "))

# my_list = [0,1]

# for i in range(2, n):
#     my_list.append(my_list[-1] + my_list[-2])
# print(my_list)


# another method memory effient

# def my_gen(n):   
#     a, b = 0, 1
#     yield a
#     for i in range(n-1):
#         yield b
#         a, b = b, a + b

# for num in my_gen(5):
#     print(num, end=' ')

# recursive methos
def rec_fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return rec_fibonacci(n-1) + rec_fibonacci(n-2)

for n in range(10):
    print(rec_fibonacci(n), end=' ')