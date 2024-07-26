lst = [2,7,4,6,1,4,9,3,8,1,10,5]

odds = [x for x in lst if x % 2 != 0]
odds.sort(reverse=True)

result = [x if x% 2 ==0 else odds.pop() for x in lst]
print(result)