
def my_decor(func):
    def inner(*args, **kwargs):
        
        print(args, kwargs)
        a = func(*args, **kwargs)
        print(a)

    return inner
        



@my_decor
def div(a, b):
    return a / b
@my_decor
def cap(st):
    return st.upper()

div(b=2, a=4)
cap('adam')



