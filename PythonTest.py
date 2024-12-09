lst1 = [1,2,3,4,5,[8,9]]
lst2 = lst1.copy()
lst1[5][0] = 0

print(lst1)
print(lst2)