'''
One night, two IIT students decided to count the number of bright stars in the northern and southern parts of the sky. We model the situation using threads.

	1) Run the students as two thread "northstud" and "southstud" where they maintain a common starcount. Each student takes about 0.01 seconds to spot a bright star.

	2) Only one of the student can update the starcount at any time.

	3) Both of the students stop counting after 5 seconds.
'''

import threading
import time

starcount = 0
myLock = threading.Lock()
myEvent = threading.Event()

def counting(lock,event):
    global starcount
    while(event.is_set() == False):
        time.sleep(0.01)
        lock.acquire()
        starcount += 1
        lock.release()
    else:
        return

northstud = threading.Thread(target=counting,args=(myLock,myEvent))
northstud.start()
southstud = threading.Thread(target=counting,args=(myLock,myEvent))
southstud.start()

time.sleep(5)

myEvent.set()

northstud.join()
southstud.join()

print('Total star count = ', starcount)
