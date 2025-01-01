arr = [-10, 8, -6, 4, -2, 5]
result = float('inf')
for x in arr:
    if not x < 0 and x < result:
        result = x
print(result)

#segregated array
arr2 = [0, 1, 0, 1, 0, 1, 0]
arr2.sort()
print(arr2)