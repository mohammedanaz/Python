
for i in range(6):
    for j in range(10):
        if j<= 5-i or j > 4 + i:
            print(' ', end='')
        else:
            print('*', end='')

    print('')