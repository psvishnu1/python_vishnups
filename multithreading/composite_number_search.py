'''
(Composite search) Given a list of 50 numbers (most of which are prime) find a composite number in this list.

Create a thread for each of the number in the list wherein the thread checks if the number is prime or not.

Make sure that the other threads are aborted as soon as an answer is found.

Use the shell command time to measure the time taken by your program.
'''

import threading

composite = 1
threads = []
found_a_comp = False

def is_composite(n):
    global found_a_comp,composite
    if (found_a_comp == False):
        if n < 2:
            return 
        else:
            for i in range(2,n):
                if (n % i == 0):
                    composite = n
                    found_a_comp = True
                    return
    else:
        return

n = 1
while n > 0:
    n = int(input())
    th = threading.Thread(target=is_composite, args=(n,))
    th.start()
    threads.append(th)


for th in threads:
    th.join()

print("Found a composite number, it is ", composite)








        
