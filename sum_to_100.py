'''
Computes sum of numbers from 1 to 100 using python threads. To do this, write a python program that perform the following

(a) Create 5 threads where each thread receives a list of 20 numbers. Then, the thread prints the list it receives and its sum.

(b) Each thread, before finishing, should update its sum in a shared global variable.

(c) Finally, print the sum.

Hint: Part(a) - Try to write a single function and create 5 threads with different arguments. Part(b) requires use of threading.Lock.
'''

import threading

NetSum = 0
MyLock = threading.Lock()


def summing(NumList,i):
    global NetSum
    print(f'Received list {i} : ',NumList)
    MySum = sum(NumList)
    print(f'Sum of list {i} = ',MySum)
    MyLock.acquire()
    NetSum += MySum
    MyLock.release()


FullList = list(range(101))
StartIndex = 1
threadList = []

for i in range(5):
    MyPart = FullList[StartIndex:StartIndex+20]
    j = threading.Thread(target = summing, args = (MyPart,i+1))
    j.start()
    threadList.append(j)
    StartIndex += 20

threadList[0].join()
threadList[1].join()
threadList[2].join()
threadList[3].join()
threadList[4].join()
print("Total sum = ", NetSum)
