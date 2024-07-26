

arr = [1,2,3,4,5,1,2,6,7,3,9]

st = 'test'

def remove_dupe(arr):
    new_lst = []
    for x in arr:
        if x not in new_lst:
            new_lst.append(x)
    return new_lst


print(remove_dupe(arr))
print(st)