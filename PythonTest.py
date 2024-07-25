def myFn(arr):
    result = [x for x in arr if ord(x.lower()) >= 97 and ord(x.lower()) <= 122]
    print(result)

arr = ['H', 'h', '@', '/', 'l', 'l', '#', 'o']
myFn(arr)