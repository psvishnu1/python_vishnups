'''
(Composite search) Given a list of 50 numbers (most of which are prime) find a composite number in this list.

Create a thread for each of the number in the list wherein the thread checks if the number is prime or not.

Make sure that the other threads are aborted as soon as an answer is found.

Use the shell command time to measure the time taken by your program.
Find out the number of threads for which the ratio of the two times is maximum (The answer will vary depending on the machine used to run the code).
'''

import multiprocessing as mp
import os

processes = []

def is_composite(n,event):
    if n < 2:
        return 
    else:
        for i in range (2,n):
                        
            if (event.is_set() == True):
                return

            elif (n % i == 0):
                composite = n
                print("Found a composite number, it is ", composite)
                event.set()
                return

n = 1
myEvent = mp.Event()

while n > 0:
    n = int(input())
    pro = mp.Process(target=is_composite, args=(n,myEvent))
    pro.start()
    processes.append(pro)

for proc in processes:
    proc.join()









        
