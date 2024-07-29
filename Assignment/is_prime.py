def is_prime(n,d=2):
    
    if n ==1:
        return False
    elif n == d:
        return True
    elif n % d == 0:
        return False
    else:
        return is_prime(n,d+1)
    

my_list = [1,2,3,4,5,6,7,8,9,10]

for x in range(len(my_list)):
    if is_prime(my_list[x]):
        my_list[x] = 'Prime'

print(my_list)