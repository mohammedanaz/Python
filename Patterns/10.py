for i in range(1, 6):
    c = i
    print('')
    for j in range(1, 10):
        if j < (6 - i) or j > (4 + i):
            print('  ', end='')
        else:
            if j <= 5:
                print(f'{c} ', end='')
                if j != 5:
                    c -= 1
            else:
                c += 1
                print(f'{c} ', end='')
