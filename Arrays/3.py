# Remove special characters in an array except for alphabets.
#     - Sample Input: {'H', 'e', '@', 'l', 'l', 'o', '#'}
#     - Sample Output: {'H', 'e', 'l', 'l', 'o'}

arr = ['H', 'e', '@', 'l', 'l', 'o', '#']

n = len(arr)
i = 0

while i < n:
    if not arr[i].isalpha():
        arr.remove(arr[i])
        n -= 1
    else:
        i += 1

print(arr)