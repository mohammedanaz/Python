def one(func = None):
    if func is None:
        return 1
    else:
        return func(1)
    
def two(func = None):
    if func is None:
        return 2
    else:
        return func(2)

def plus(x):
    def anony(y):
        return x +y
    
    return anony

print(one(plus(two())))