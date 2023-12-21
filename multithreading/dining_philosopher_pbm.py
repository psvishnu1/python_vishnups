'''
Implement the dining philosopher problem with three philosophers and three chopsticks. Illustrate how deadlock can arise in your code and explain why they arise.
'''

from concurrent.futures import thread
import threading
import time

chopStick1 = threading.Lock()
chopStick2 = threading.Lock()
chopStick3 = threading.Lock()
food = 100

def eat(name, left, right):
    global food

    while (food > 0):
        print(f'{name} requires 2 chopsticks to start eating')
        left.acquire()
        print(f'{name} got one chopstick, waiting for other')
        right.acquire()
        print(f' {name} got both chopsticks, now going to eat')
        if ( food > 0 ):
            food -= 1
            print(name, "ate food. Remaining", food)
        
        left.release()
        right.release()



threading.Thread(target=eat, args=("Philosopher 1", chopStick1, chopStick2)).start()
threading.Thread(target=eat, args=("Philosopher 2", chopStick2, chopStick3)).start()
threading.Thread(target=eat, args=("Philosopher 3", chopStick3, chopStick1)).start()
