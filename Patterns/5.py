
for i in range(1, 6):
    print('')
    for j in range(1, 6):
        if j < (6 - i):
            print(' ', end='')
        else:
            print('*', end='')


print('\n')

for i in range(1, 6):
    print('')
    for j in range(1, 6):
        if j < i:
            print(' ', end='')
        else:
            print('*', end='')
