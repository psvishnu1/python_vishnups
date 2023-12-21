'''
Answer to Qn 2: Printing first N special primes
A prime number p is called special if p + 1 is a power of 2. Write a python program to read a number n from the user and print the first n special primes. Test the code with n being 4 or 5.

Examples:

Input: n=1 should give output as 3
Input: n=2 should give output as 3, 7
Input: n=3 should give output as 3, 7, 31
'''

N = int(input('Enter N = '))        # Number of special primes to be printted

def isPrime(num):                   # Function to check a number is prime or not
    count = 0
    for i in range(2,num+1):
        if (num % i == 0):
            count += 1
    if (count == 1):
        return True
    else:
        return False

def isPowerTwo(num):                # Function to check a number is power of 2 or not
    while (num % 2 == 0):
        num /= 2
    if (num == 1):
        return True
    else:
        return False

MyPrime = 2
SpPrime = []                        # list to collect all special primes
i = 0
while(i != N):
    if (isPrime(MyPrime) == True and isPowerTwo(MyPrime+1) == True):    # Checking whether number is prime and number+1 is power of 2
        SpPrime.append(MyPrime)
        MyPrime += 1
        i += 1
    else:
        MyPrime += 1

for k in SpPrime:                   # Printing special primes separated by space
    print(k, end =" ")
print("")                           # To bring cursor to next line
