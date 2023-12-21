'''
Deepak and Dinesh have accounts in the Bank of IITPKD. The two joint accounts account_1 and account_2 with account_1 having Rs 100 and account_2 having Rs 200. 
One day, Dinesh decides to transfer Rs 100 from account_2 to account_1 and the same day Deepak decides to transfer Rs 200 from account_1 to account_2. But it is not clear which order will the bank process it.

Model the transactions as two threads - Dinesh and Deepak. Dinesh and Deepak threads would wait for uniformly random time from the interval [2,3] seconds before initiating the transfer.

Create a function bank(sender_account, receiver_account, amount) which will be called by the two threads whenever it wants to do transaction. 
This function will decline a request should the balance in any of the accounts go below 0. Bank function reports all the transactions and the account balances at the end of each transaction.

bank() function should ensure that it is not interrupted in the middle of a transaction.

Sample output is either of the following: 

Sample run 1

Dinesh: transfer Rs 100 from account_2 to account_1
Bank: Balance of account_1 is 200 and account_2 is 100
Deepak: transfer Rs 200 from account_1 to account_2
Bank: Balance of account_1 is 0 and account_2 is 300

Sample run 2

Deepak: transfer Rs 200 from account_1 to account_2
Bank: Transaction declined. account_1 has insufficient balance.
Dinesh: transfer Rs 100 from account_2 to account_1
Bank: Balance of account_1 is 200 and account_2 is 100
'''

import threading
import time
import random

account_1 = 100
account_2 = 200
lockerKey = threading.Lock()

def bank(sdr_acc,rxr_acc,amt,name):
    global account_1,account_2
    waitTime = random.uniform(2,3)
    time.sleep(waitTime)
    lockerKey.acquire()
    if ( sdr_acc == 'account_1' and (account_1-amt) < 0 ):
        print('Bank: Transaction declined. account_1 has insufficient balance.')
        lockerKey.release()
        return
    elif ( sdr_acc == 'account_2' and (account_2-amt) < 0 ):
        print('Bank: Transaction declined. account_2 has insufficient balance.')
        lockerKey.release()
        return
    else:
        if (sdr_acc == 'account_1'):
            account_1 -= amt
            account_2 += amt
        elif (sdr_acc == 'account_2'):
            account_2 -= amt
            account_1 += amt
        print(f'Balance of account_1 is {account_1} and account_2 is {account_2}')
        lockerKey.release()
        return

Dinesh = threading.Thread(target=bank,args=('account_2','account_1',100,'Dinesh'))
Deepak = threading.Thread(target=bank,args=('account_1','account_2',200,'Deepak'))


Dinesh.start()
print('Dinesh: transfer Rs 100 from account_2 to account_1')
Deepak.start()
print('Deepak: transfer Rs 200 from account_1 to account_2')

Dinesh.join()
Deepak.join()

