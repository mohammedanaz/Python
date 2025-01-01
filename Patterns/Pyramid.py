
for i in range(1, 6):
    for j in range(1, 10):
        if j<= 5-i or j > 4 + i:
            print(' ', end='')
        else:
            print('*', end='')

    print('')

print('')

for i in range(1, 6):
    for j in range(1, 10):
        if j<i or j > 10 - i:
            print(' ', end='')
        else:
            print('*', end='')

    print('')

print('')

for i in range(1, 6):
    flag = 1
    for j in range(1, 10):
        if j<= 5-i or j > 4 + i:
            print(' ', end='')
        else:
            if flag:
                print('*', end='')
                flag = 0
            else:
                print(' ', end='')
                flag = 1

    print('')
