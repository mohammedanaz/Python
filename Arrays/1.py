#Rearrange positive and negative numbers alternatively.
#    - Sample Input: {-1, 2, -3, 4, -5, 6, -7}
#    - Sample Output: Rearranged array: 2 -3 4 -5 6 -1 -7

arr = [-1, 2, -3, 4, -5, 6, -7, 3, 6, 8, 10]
arr.reverse()

pos = []
neg = []
result = []
for x in arr:
    if x < 0:
        neg.append(x)
    else:
        pos.append(x)

itr = min(len(pos), len(neg))
for i in range(itr):
    a = pos.pop()
    b = neg.pop()
    result.append(a)
    result.append(b)
if pos:
    result.extend(pos)
if neg:
    result.extend(neg)

print(result)