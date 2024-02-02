def find_factorial(num):
    if num == 1:
        return 1
    else:
        return num * find_factorial(num-1)
    
print(find_factorial(10))