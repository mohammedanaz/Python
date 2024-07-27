def my_fn(*args, **kwargs):
    
    value = kwargs.get('name')
    if value:
        print(value)
    else:
        print('no such key')

my_fn(temp='Adam')