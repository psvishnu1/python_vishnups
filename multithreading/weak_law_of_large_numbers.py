'''
Write a program to see the weak law of large numbers in action using random library in python.

	1) To do this, we use a main thread and five other threads. All the threads share a common queue.

	2) We now describe what the five threads do. Each of these five threads, pushes 10000 uniformly random number from the set [0, 1, 1947, 2022] into the queue and exits. Note that the mean of this distribution is 992.50

	3) The main thread examines the queue and computes the average of the numbers seen so far from the queue. Once a thread exists after pushing 10000 numbers, the main prints the value of the average it maintains.

	4) As more and more threads exits, the average value printed by the main thread should become closer and closer to 992.50.

[Hint: Use random.choice to sample a number from a given set ]
'''

import threading
import random
import queue

myQue = queue.Queue()
myThreads = []
myEvent = threading.Event()
mySum = 0
myAvg = 0
myN = 0

def push2Que(event):
    for i in range(10000):
        num = random.choice([0,1,1947,2022])
        myQue.put(num)
    event.set()
    return

for i in range(5):
    th = threading.Thread(target=push2Que,args=(myEvent,))
    th.start()
    myThreads.append(th)

while(myQue.empty() == False):
    mySum += myQue.get()
    myN += 1
    myAvg = mySum / myN
    if (myEvent.is_set() == True):
        print('Average = ', myAvg)
        myEvent.clear()

for i in myThreads:
    i.join()

print('Average = ', myAvg)


