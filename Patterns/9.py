
for i in range(1, 4):
    print('')
    for j in range(1, 10):
        if j == (4 - i) or j == (8 - i) or j == (2 + i) or j == (6 + i):
            print('*', end='')
        else:
            print(' ', end='')