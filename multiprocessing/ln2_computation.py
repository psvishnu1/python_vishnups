'''
Do parallel computation to compute ln(2) using the formula 1-1/2+1/3-1/4+... by computing the first 10000 terms in the above sum
'''

import multiprocessing as mp
import os
from queue import Queue

processes = []
start = 1
end = 10000
totalSum = 0

def ln2(a,b,q):
    i = 0
    localSum = 0
    while (a<b):
        localSum += ( ((-1)**i) * (1/a))
        a += 1
        i += 1
    q.put(localSum)
    return

myQue = mp.Queue()

for i in range(100):
    start_val = start + (i*100)
    end_val = start + ((i+1)*100)
    pro = mp.Process(target=ln2,args=(start_val,end_val,myQue))
    pro.start()
    processes.append(pro)

for pr in processes:
    pr.join()

while(myQue.empty() == False):
    totalSum += myQue.get()

print('Log 2 value is =',totalSum)
        
