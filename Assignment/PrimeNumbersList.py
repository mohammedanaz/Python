def prime_checker(n,d=2):
    if n ==1:
        return False
    elif n == d:
        return True
    elif n % d == 0:
        return False
    else:
        return prime_checker(n,d+1)

prime_list = []

def prime_maker(limit):
    for x in range(1, limit+1):
        if prime_checker(x):
            prime_list.append(x)
    print(prime_list)

prime_maker(19)