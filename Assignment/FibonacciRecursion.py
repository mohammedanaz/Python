# 0,1,1,2,3,5,8,13,21

def fbn(n, a=0, b=1, count=2):
    
    if n == 1:
        return 0
    if n == 2:
        return 1
    if n > 2:
        if count == n:
            return b
        else :
            a,b = b, a+b
            return fbn(n,a,b,count+1)

print(fbn(9))