arr1 = [1,5,10,20,40,80]
arr2 = [6,7,20,80,100]
arr3 = [3,4,15,20,30,70,80,120]

result = []

for x in arr3:
    if x in arr2 and x in arr1:
        result.append(x)

print(result)

# i,j,k = 0,0,0
# result = []

# while i<len(arr1) and j<len(arr2) and k<len(arr3):
#     if arr1[i] == arr2[j] == arr3[k]:
#         result.append(arr1[i])
#         i+=1
#         j+=1
#         k+=1
#     elif arr1[i] < arr2[j]:
#         i+=1
#     elif arr2[j] < arr3[k]:
#         j+=1
#     else:
#         k+=1

# print(result)