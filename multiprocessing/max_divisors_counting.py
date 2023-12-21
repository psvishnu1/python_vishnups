'''
Write a program that takes a list of numbers as input and outputs the number with the maximum number of divisors.

	1) For example, if the input list is [40, 60, 80] then the answer is 60 (as 60 has 10 divisors and others have less than 10 divisors).

	2) The user should input the length of the list first followed by the list of numbers. Then, use the multiprocessing library of python to start a new process that computes the number of divisors and store it in a queue.

	3) Once all the processes completes the main thread inspects the queue and prints the number with the largest number of divisors.
'''

import multiprocessing as mp
from queue import Queue

myQue = mp.Queue()
myList = []
processList = []
largestDiv = 0
largestNum = 0


def findDivNum(n,q):
    numDiv = 0
    for i in range(1,n):
        if (n%i == 0):
            numDiv += 1
    q.put([n,numDiv])

myLen = int(input('Enter length of list = '))
print('Enter numbers in list one by one: ')
for i in range(myLen):
    myList.append(int(input()))

for j in range(myLen):
    pro = mp.Process(target=findDivNum,args=(myList[j],myQue))
    pro.start()
    processList.append(pro)

for k in processList:
    k.join()

while(myQue.empty()==False):
    t = myQue.get()
    if (t[1]>largestDiv):
        largestDiv=t[1]
        largestNum=t[0]

print(f'Number with most divisors is {largestNum} and its number of divisors is {largestDiv}')
