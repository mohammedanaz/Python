arr = [5, 8, 2, 10, 15, 4]
arr.sort()
left = 0
right = len(arr) - 1
result = []
while left < right:
    result.append(arr[left])
    result.append(arr[right])
    left += 1
    right -= 1

print(result)

len()
