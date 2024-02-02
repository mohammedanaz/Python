def prime(n,d=2):
    
    if n <= d:
        return True
    elif n % d == 0:
        return False
    else:
        return prime(n,d+1)
    

my_list = [1,2,3,4,5,6,7,8,9,10]

for x in range(len(my_list)):
    if prime(my_list[x]) and my_list[x] != 1:
        my_list[x] = 0

print(my_list)