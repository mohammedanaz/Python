def calculateSum(n):
    sum = 0
    for x in range(1,n):
        if x % 2 == 0:
            sum += x 
    print(sum)

calculateSum(10)