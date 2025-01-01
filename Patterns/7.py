
for i in range(1, 8):
    print('')    
    x = i
    y = 8 - i
    for j in range(1, 8):
        if i <= 4:
            if j < (5 - i ) or j > (3 + i):
                print(' ', end='')
            else:
                print(x, end='')
                if j < 4:
                    x -= 1
                if j >= 4:
                    x += 1
        else:
            if j < (i - 3) or j > (11 - i):
                print(' ', end='')
            else:
                print(y, end='')
                if j < 4:
                    y -= 1
                if j >= 4:
                    y += 1