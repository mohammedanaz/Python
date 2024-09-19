arr = ['iah woh era uoy', 'aaa fde ffrt']
result =[]


for x in arr:
    split_x = x.split()
    temp = []
    s = ''
    print(split_x)
    for y in split_x:
        temp.append(y[::-1])
    s = ' '.join(temp)
    result.append(s)

print(result)