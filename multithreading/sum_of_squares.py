'''
Write a program that uses threads to compute sum of square of numbers in two lists of same length.

For example, if the first list is [1, 2, 3] and second list is [-1, 0 ,1], then the output should be 14 (from the one thread) and 2 (from the other thread) respectively.

The main thread asks the user to enter the length of the list and then asks to enter the numbers in first list followed by the numbers in the second list

The thread for the second list is to be started first, followed by the thread for first list. But the output of the first list should be printed first.
'''

import threading

a = []
b = []

sem = threading.Semaphore(0)

def square(L,num):
    mySum = 0
    for i in L:
        mySum += (i**2)
    if (num == 2):
        sem.acquire()
        print(f'Sum of squares of list {L} is {mySum}')
    else:
        sem.release()
        print(f'Sum of squares of list {L} is {mySum}')


n = int(input('Enter length of lists: '))

print('Enter numbers in first list: ')
for i in range(n):
    a.append(int(input()))

print('Enter numbers in second list: ')
for i in range(n):
    b.append(int(input()))

t2 = threading.Thread(target=square,args=(b,2))
t2.start()
t1 = threading.Thread(target=square,args=(a,1))
t1.start()

t1.join()
t2.join()
