'''
In a tea shop, the tea maker dozes off when there are no customers. As customers come, tea maker wakes up and prepares tea. 
If there is another customer, tea is prepared again otherwise the tea maker goes back to sleep. Tea maker takes 1 second to prepare the tea and cannot handle more than 2 orders.

Consider the situation where 10 customers come to the shop after a delay of 3 seconds. Think of teamaker as the main thread and 10 customer as other threads.

(a) Model the scenario of the teamaker customer interaction using threads and queues. Sample output when there are only 3 customers is as follows: 

Tea maker: Ready
Tea maker: No customer. So dozzing off ...
Customer 1: arrives
Customer 2: arrives
Tea maker: Prepares tea for Customer 1
Tea maker: Prepares tea for Customer 2
Customer 3: arrives
Customer 1: drinks tea and leaves
Customer 2: drinks tea and leaves
Tea maker: Prepares tea for Customer 3
Customer 3: drinks tea and leaves
Tea maker: No customer. So dozzing off ...
(b) Modify the above program so that the average waiting time of all the customers is computed and printed. Waiting time of each customer is the time taken for it to receive the tea after the thread starts. 
'''

import threading
import time
import random
import queue

serving_que = queue.Queue()
customers = []
maxCount = threading.Semaphore(2)
startTime = []
endTime = []
totWaittime = 0

def customer(cust_num,maxC):
    global serving_que,customers,startTime,totWaittime
    print(f'Customer {cust_num}: arrives')
    while ( serving_que.empty == True ):
        pass
    k = serving_que.get()
    print(f'Customer {k}: drinks tea and leaves')
    t2 = time.time()
    waitTime =  t2 - startTime[k-1]
    totWaittime += waitTime
    customers.pop()
    maxC.release()
    return


print('Tea maker: Ready')
print('Tea maker: No customer. So dozzing off')
time.sleep(3)
for h in range(10):
    myCustomer = threading.Thread(target=customer,args=(h+1,maxCount))
    customers.append(myCustomer)

for k in customers:
    k.start()
    startTime.append(time.time())


for i in range(len(customers)):
    maxCount.acquire()
    print(f'Tea maker: Prepares tea for customer{i+1}')
    time.sleep(1)
    serving_que.put(i+1)
for j in customers:
    j.join()

print('Tea maker: No customer. So dozzing off')
print('average wait time per customer = ',totWaittime/10)
