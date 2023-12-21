'''
The following question asks to perform matrix multiplication using multiprocessing in two ways and compare them. First, get a value of n as input and get two n x n matrices A and B from the user. Then, compute the matrix product in the following two ways.

(a) Compute each of the n*n entries by having a separate threads for each output entry of the product. In total, this method uses n*n threads. (Save this as q3a.py)

(b) Compute each of the n rows by having a separate thread that for computing all the entires of a row of the product. In total, this method uses n threads. (Save this as q3b.py)

For both (a) and (b) use Queues provided by multiprocessing to collect the results from each of the process.

Compute the time taken to obtain the product for various values of n (starting from 2,3 ...) for both the methods (a) and (b). Compare them and check which is better and explain why ?

You may want to write the input matrices in a file and use input redirection (<)
'''

import multiprocessing as mp
from queue import Queue
import os


matrixSize = 0
processes = []


def matrixMul(a,b,i,j,q,n):
    temp = 0
    for r in range(n):
        temp += ( a[r] * b[r] )
    q.put([i,j,temp])
    return
  


matrixSize = int(input())
matA = [[0 for i in range(matrixSize)] for j in range(matrixSize)]
matB = [[0 for i in range(matrixSize)] for j in range(matrixSize)]
matF = [[0 for i in range(matrixSize)] for j in range(matrixSize)]

for i in range(matrixSize):
    for j in range(matrixSize):
        temp = input().split()
        matA[i][j] = int(temp[0])
        matB[i][j] = int(temp[1])

myQue = mp.Queue()

for i in range(matrixSize):
    for j in range(matrixSize):
        a = matA[i]
        b = []
        for l in matB:
            b.append(l[j])
        pro = mp.Process(target=matrixMul,args=(a,b,i,j,myQue,matrixSize))
        pro.start()
        processes.append(pro)

for pro in processes:
    pro.join()

while (myQue.empty() == False):
    C = myQue.get()
    matF[C[0]][C[1]] = C[2]
    

print('Matrix A x B =', matF)
