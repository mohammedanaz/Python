
def custom_range(*args):
    arg_length = len(args)

    if arg_length < 1:
        raise TypeError('Must have atleast one argument.')
    if arg_length > 3:
        raise TypeError(f'Custom range expect max 3 args but {arg_length} is given.')
    if args[0] >= args[1]:
        raise TypeError(f'Start should be less than end.')
    if arg_length:
        for x in args:
            if type(x) != int:
                raise TypeError('args should be an integer')
    if arg_length == 1:
        start = 0
        stop = args[0]
        step = 1
    if arg_length == 2:
        start = args[0]
        stop = args[1]
        step = 1
    if arg_length == 3:
        start = args[0]
        stop = args[1]
        step = args[2]


    while start < stop:
        result = start
        yield result
        start += step 
try:
    for x in custom_range(100, 200, 3):
        print(x, end=' ')
except Exception as e:
    print(str(e))
