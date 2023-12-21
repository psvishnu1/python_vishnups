'''
Write a program to calculate the value of pi. To do this, sample two number x and y from a uniform distribution from [-1,1] and the pair (x,y) is inside a unit circle x**2 + y**2 <= 1. 
Repeat this for N times for N = 300, 3000, 30000. For each of the iterations find the number of times the point falls inside the unit circle, say count. Output 4*count/N as the approximation for pi.

Note that the probability that the point falls inside the circle is the area of the circle divided by area of the square. Hence 4 times an estimate of this quantity is an estimate of pi.

(a) Do the counting by creating 3 threads. All the threads updates the same global count variable. Measure the time taken using time program in the shell. 

(b) Do the same using 3 processes. Note that the same method of using a global count as in part (a) does not work as processes do not share memory space. 
Use a queue to update the counts and let the main process compute the final value. Measure the time taken and calculate the speedup achieved. 
'''

import threading
import random

count = 0
thredList = []
myLock = threading.Lock()

def myVal(n,myLock):
    global count
    for i in range(n):
        x = random.uniform(-1,1)
        y = random.uniform(-1,1)
        if ((x**2 + y**2) < 1):
            myLock.acquire()
            count += 1
            myLock.release()
        
N = 3000
num_threads = N//3
for j in range(3):
    th = threading.Thread(target=myVal,args=(num_threads,myLock))
    th.start()
    thredList.append(th)

for h in thredList:
    h.join()

res = 4*(count/N)
print(res)
