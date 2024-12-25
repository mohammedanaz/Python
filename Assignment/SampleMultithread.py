import time
from threading import Thread

result = [[],[]]
def squere(arr):
    global result
    for x in arr:
        print('Squre - ', x*x)
        result[0].append(x*x)
        time.sleep(0.5)

def cube(arr):
    for x in arr:
        print('Cube - ', x*x*x)
        result[1].append(x*x*x)
        time.sleep(0.5)

arr = [1, 2, 3, 4]
t1 = Thread(target=squere, args=(arr,))
t2 = Thread(target=cube, args=(arr,))

tm =time.time()
t1.start()
t2.start()

t1.join()
t2.join()

print('result -', result)
print(time.time() - tm)