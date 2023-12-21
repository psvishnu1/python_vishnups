'''
(Search for a pair with common factor) In this question, we are given a list of 50 distinct numbers with most pairs being co-prime. You have to find a pair of numbers from the list that have a common divisor larger than 1.

To do this, create a new thread for each pair of numbers from the list. Each of the threads checks if the pair of numbers have a common divisor. Checking for a common divisor can be done using math.gcd.

Make sure that the other threads are aborted as soon as an answer is found.

Test your code with the following 50 pairs from the file 50coprime.txt in the same. 
Find out the number of threads for which the ratio of the two times is maximum. The answer will vary depending on the machine used to run the code.
'''

import multiprocessing as mp
import math

processes = []
numbers = []


def is_noncoprime(a,b,event):
    if ( event.is_set() == False):
        Gcd = math.gcd(a,b)
        if Gcd>1:
            print("Found a pair having common divisor larger than 1, the pair is : ",[a,b] ," and GCD = ",Gcd)
            event.set()
            return
    else:
        return

n = 1
while n > 0:
    n = int(input())
    numbers.append(n)

numbers.remove(0)
myEvent = mp.Event()

for i in range(len(numbers)-1):
    for j in range(i+1,len(numbers)):
        pro = mp.Process(target=is_noncoprime, args=(numbers[i],numbers[j],myEvent))
        pro.start()
        processes.append(pro)


for pro in processes:
    pro.join()
        
