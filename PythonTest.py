
def isPrime(n):
    if n < 4:
        return True
    else:
        for i in range(2, n):
            if n % i == 0:
                return False
        return True
    
print(isPrime(11))