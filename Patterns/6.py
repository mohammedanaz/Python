
for i in range(1, 6):
    print('')
    for j in range(1, 10):
        if j == (6 - i) or j == (4 + i) or i == 5:
            print('*', end='')
        else:
            print(' ', end='')