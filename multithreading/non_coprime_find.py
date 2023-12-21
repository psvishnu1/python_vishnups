'''
(Search for a pair with common factor) In this question, we are given a list of 50 distinct numbers with most pairs being co-prime. 
You have to find a pair of numbers from the list that have a common divisor larger than 1.

To do this, create a new thread for each pair of numbers from the list. Each of the threads checks if the pair of numbers have a common divisor. Checking for a common divisor can be done using math.gcd.

Make sure that the other threads are aborted as soon as an answer is found.

Test your code with the following 50 pairs from the file 50coprime.txt in the same (week07) folder.
'''

import threading
import math

myPair = []
threads = []
numbers = []
found_a_pair = False
Gcd = 0

def is_noncoprime(a,b):
    global found_a_pair,myPair,Gcd
    if (found_a_pair == False):
        Gcd = math.gcd(a,b)
        if Gcd>1:
            myPair.extend([a,b]) 
            found_a_pair = True


n = 1
while n > 0:
    n = int(input())
    numbers.append(n)
    # print(numbers)

numbers.remove(0)

for i in range(len(numbers)-1):
    for j in range(i+1,len(numbers)):
        th = threading.Thread(target=is_noncoprime, args=(numbers[i],numbers[j]))
        th.start()
        threads.append(th)


for th in threads:
    th.join()

print("Found a pair having common divisor largre than 1, the pair is ", myPair," and GCD = ",Gcd)








        
