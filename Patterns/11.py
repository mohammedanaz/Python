#print(chr(69))


for i in range(1, 6):
    print()
    c = 70 - i
    for j in range(1, i+1):
        print(chr(c), ' ', end='')
        c += 1