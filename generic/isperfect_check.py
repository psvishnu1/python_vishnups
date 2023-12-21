'''
Write a function isPerfect() to check if a number is perfect. A number is perfect if the number is equal to the sum of all its positive divisors less that itself. For example 6 is perfect as 6 = 1 + 2 + 3.
'''

def isPerfect():
    sum = 0
    num = int(input('Enter your number: '))
    for i in range(1,num):
        if(num % i == 0):
            sum += i

    if (sum == num):
        print('The number you entered is perfect')
    else:
        print('The number you entered is not perfect')

isPerfect()
