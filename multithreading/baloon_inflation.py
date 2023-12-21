'''
Model the following scenario using python threads.

Two children are inflating small balloons. Each child takes a uniformly random time (in seconds) from the interval [2.5, 3] to inflate one balloon.
The task is to count the total number of ballons inflated.

Hint: Use random.uniform to get a uniform random time and time.sleep to simulate the time to inflate. Use threading.Lock to maintain the count correctly.
Also test your code with intervals like [0, 0.001] to ensure that the count is correct.
'''

import threading
import time
import random

MyLock = threading.Lock()
BaloonCount = 100

def inflating(name,i):
    global BaloonCount
    chCount = 0
    while(BaloonCount > 1):
        InfTime = random.uniform(0,0.001)
        time.sleep(InfTime)
        MyLock.acquire()
        BaloonCount -= 1
        MyLock.release()
        chCount += 1
    print(f'number of baloons inflated by child {i} = ',chCount)
child1 = threading.Thread(target = inflating,args = ("Child 1",1))
child1.start()
child2 = threading.Thread(target = inflating,args = ("Child 2",2))
child2.start()
child1.join()
child2.join()
print("finished inflating")

