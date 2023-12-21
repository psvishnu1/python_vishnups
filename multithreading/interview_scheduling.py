'''
(Interviews) Imagine an ongoing placement session with 4 interview rooms. There are 10 candidates to be interviewed. Each interview lasts for t minutes where t follows a normal distribution with mean 4 and variance 0.2. In this question, we aim to model this situation using threads.

Only one candidate can be in an interview room and a candidate can get in if nobody is being interviewed. Once all the 4 rooms are occupied, others have to wait till a room becomes available.

For the purpose of implementation, each candidate takes t seconds (instead of t minutes).

Hint: Run each candidate as a thread and use semaphores to model the interview rooms. Use random.normalvariate to sample from a normal distribution
'''

import threading
import time
import random

threads = []

sem = threading.Semaphore(4)

def interview(number):
    sem.acquire()
    print(f'Interview of candidate number {number} started')
    t = random.normalvariate(4,0.2)
    time.sleep(t)
    print(f'Interview of candidate number {number} over')
    sem.release()

for i in range(1,11):
    th1 = threading.Thread(target=interview,args=(i,))
    th1.start()
    threads.append(th1)

for i in threads:
    i.join()
