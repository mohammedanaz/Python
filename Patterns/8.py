
for i in range(1, 11):
    print('')
    if i <= 5:
        for j in range(1, 11):
            if j > (6 - i) and j < (5 + i):
                print(' ', end='')
            else:
                print('*', end='')
    else:
        for j in range(1, 11):
            if j > (i - 5) and j < (16 - i):
                print(' ', end='')
            else:
                print('*', end='')