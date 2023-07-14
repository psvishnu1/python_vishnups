number = input('Enter a Positive Integer:')
number = int(number)

def isPrime(number):
    count = 0
    for i in range(1,number+1):
        if (number % i == 0):
            count=count+1
    if (count==2):
        print("YES")
    else:
        print("NO")

isPrime(number)
