'''
	Question: Write a program to create a list named primes of prime numbers up to a given number n. Check if one plus the product of the numbers in this list is a prime number.
			  Optimise the above program so that when you are checking to see if a number i is prime you only check for divisibility by the prime numbers less than i (which are already there in the list primes)
'''

import math

N = int(input('Enter a positive number N: '))                                        #Taking Input and Initialization
primes = []

def is_prime(number):                                                       #Function to check prime or not
    count = 0
    for i in range(2,number+1):
        if (number % i == 0):
            count=count+1
    if (count==1):
        return(True)
    else:
        return(False)

for i in range(2,N+1):                                                      #Loop calls is_prime function for each number upto N
    if (is_prime(i) == True):
        primes.append(i)

print(f'Prime numbers upto {N} are {primes}')                               #Printing list of prime number upto N

if (primes == []):                                                          #checking 1+prod(primes) is prime or not, if condition is because even if list empty math.prod returns 1
    k=(math.prod(primes))
else:
    k=(1+math.prod(primes))

# if(is_prime(k)==True):                                                    #Before Optimiation:
#     print(f'1 + product of numbers in the list = {k} which is also prime')
# else:
#     print(f'1 + product of numbers in the list = {k} which is Non-prime')

flag = 0                                                                    #After Optimization:
for j in primes:
    if (k % j == 0):
        flag += 1
if ((flag == 0) and (primes != [])):
    print(f'1 + product of numbers in the list = {k} which is also prime')
else:
    print(f'1 + product of numbers in the list = {k} which is Non-prime')    
