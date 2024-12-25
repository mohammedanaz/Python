from multiprocessing import Process
import time

result = []

def Squared(arr):
    global result
    for x in arr:
        print('Square - ', x*x)
        time.sleep(2)
        result.append(x*x)
    print('Result inside Fn - ', result)

def Cube(arr):
    global result
    for x in arr:
        print('Cube - ', x*x)
        time.sleep(2)
        result.append(x*x*x)
    print('Result inside Fn - ', result)

if __name__ == '__main__':

    arr = [1,2,3,4,5]
    p1 = Process(target=Squared, args=(arr,))
    p2 = Process(target=Cube, args=(arr,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print('Result is -', result)
