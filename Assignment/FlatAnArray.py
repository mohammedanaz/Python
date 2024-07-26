
lst = [1,2,[11,13],['Hi'],9]

result = []

for x in lst:
    if type(x) == list:
        for i in x:
            result.append(i)
    else:
        result.append(x)

print(result)

