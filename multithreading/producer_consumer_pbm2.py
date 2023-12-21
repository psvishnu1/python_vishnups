'''
Implement the producer consumer problem with one producer (called G) and one consumer (called C) using threading.Events

Write a program that has 2 threads namely: G and C threads. These threads exhibit the following behavior:

	1) G thread generates events, whereas C thread consumes them.

	2) G thread generates a new event t seconds after the consumption of an event. For each event, t is a random variable sampled uniformly from the set {1, 2, 3, 4, 5} (values in seconds).

	3) G thread generates only one event at a time. If an unconsumed event is present, G thread waits for C thread to consume it before generating a new event.

	4) As soon as an event occurs, C thread starts to consume it. It takes t seconds to consume an event. For each event, t is a random variable sampled uniformly from the set {1, 2, 3, 4, 5} (values in seconds).

	5) G thread should generate a total of 10 events. This number is an information private to G thread is not shared with C thread.

	6) C thread should print an appropriate message after it finishes consuming all events.
'''

import threading
import random
import time

finish = False

def MyEvent(event, name):
    global finish
    i = 0
    totTime = 0
    if (name == 'G'):
        while(i<10):
            while(event.is_set() == False):
                t1 = random.randint(1,2)
                print(f'Time {totTime}s: Event scheduled at {totTime + t1}s')
                time.sleep(t1)
                event.set()
                i += 1
                totTime += t1
                print(f'Time {totTime}s: Event occured')
        finish = True

    if (name == 'C'):
        while(finish == False):
            event.wait()
            t2 = random.randint(1,2)
            time.sleep(t2)
            event.clear()
            totTime += t2
            print(f'Time {totTime}s: Event processed')
 
event = threading.Event()

G = threading.Thread(target = MyEvent,args= (event,'G'))
G.start()
C = threading.Thread(target = MyEvent,args= (event,'C'))
C.start()
G.join()
