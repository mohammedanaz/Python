
for i in range(1, 10):
    print('')
    if i <= 5:
        for j in range(1, i+1):
            print('*', end='')
    else:
        for j in range(1, 11 - i):
            print('*', end='')