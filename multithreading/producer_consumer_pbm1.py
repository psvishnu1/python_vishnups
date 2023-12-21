'''
Implement producer consumer problem with two producers and one consumer using threading.Lock. The producers outputs in a list of size 5.

The producers cannot produce if the list is full and the consumer cannot consume if the list is empty.

Please do not use python queue for this question.
'''

import threading
import random
import time

MyLock = threading.Lock()
commodity = []
work_time = True

def store(user_type,name):
    global commodity,work_time
    print('length of comm = ',len(commodity))
    while(work_time == True):
        if (user_type == 'producer' and len(commodity)<5):
            MyLock.acquire()
            MyPdt = random.randint(1,100)
            commodity.append(MyPdt)
            print(f'Producer {name} has produced one commodity namely {MyPdt} and it is added to store')
            MyLock.release()
        elif (user_type == 'consumer' and len(commodity)>0):
            MyLock.acquire()
            ConsumedPdt = commodity.pop(0)
            print(f'Consumer has consumed an item namely {ConsumedPdt}')
            MyLock.release()

print('store opened')  
prd1 = threading.Thread(target = store,args = ("producer",1))
prd1.start()
prd2 = threading.Thread(target = store,args = ("producer",2))
prd2.start()
cnsmr = threading.Thread(target = store,args = ("consumer",1))
cnsmr.start()
time.sleep(0.5)
work_time =False
prd1.join()
prd2.join()
cnsmr.join()
print("store closed")
