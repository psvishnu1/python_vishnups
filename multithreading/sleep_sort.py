'''
(Sleep sort) Implement a sorting algorithm using time.sleep and threading.Threads which sorts positive numbers in ascending order.

Write a function sleep_and_print(n) that takes a number n as argument and does the following: sleep for n seconds, following which it prints n.

Take a list of positive numbers (with the list ending at 0) as input. After getting the entire input, for each number in the list, create a new thread which runs sleep_and_print with argument as n.
'''

import threading
import time

threads = []

def sleep_and_print(n):
    time.sleep(n)
    print(n)

numbers = input("Enter a list of numbers separated by space and ending with zero: ").split()
numbers.remove("0")
print("my numbers",numbers)
for i in range(len(numbers)):
    numbers[i] = int(numbers[i])

for i in numbers:
    t = threading.Thread(target=sleep_and_print,args=(i,))
    t.start()
    threads.append(t)

for th in threads:
    th.join()
