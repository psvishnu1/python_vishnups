'''
Write a program that uses threads in the following way:

	1) the main thread takes a number n from 1 to 5 as input and sleeps for two seconds.

	2) After two seconds it, starts 5 threads where each of the thread sleeps for 0.2 second and prints the thread number following which it again goes back to sleep for 0.2 second and repeats. The thread number is to be passed as argument to the thread while creating the thread.

	3) After starting all the five threads, the main thread sleeps again for two seconds and terminates all threads except the thread n.

A sample run is given below.

Enter a number from 1 to 5
5
Thread 1 running
Thread 3 running
Thread 2 running
Thread 4 running
Thread 5 running
Thread 1 running
Thread 3 running
Thread 2 running
Thread 4 running
Thread 5 running
Main thread killing all threads except thread 5
Thread 5 running
Thread 5 running
Thread 5 running
'''

import threading
import time

myThreads = []
myEvents = []

def myThread(num,event):
    while (event.is_set() == False):
        time.sleep(0.2)
        print(f'Thread {num} running')
    else:
        return

n = int(input('Enter a number from 1 to 5: '))

time.sleep(2)

for i in range(5):
    eve = threading.Event()
    th = threading.Thread(target=myThread,args=(i+1,eve))
    th.start()
    myEvents.append(eve)
    myThreads.append(th)

time.sleep(2)
myEvents.pop(n-1)
print('Main thread killing all threads except ', n)
for j in myEvents:
    j.set()

for k in myThreads:
    k.join()
