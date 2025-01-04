# Find the number of pairs in a given array whose sum is equal to a specified number.
#    - Sample Input: {3, 7, 2, 9, 1, 4, 6, 5}, target = 10
#    - Sample Output: Number of pairs with sum 10: 3

arr = [3, 7, 2, 9, 1, 4, 6, 5]
target = 10
freq = {}
count = 0
for x in arr:
    diff = target - x
    if diff in freq:
        count += freq[diff]
    freq[x] = freq.get(x, 0) + 1

print(count)