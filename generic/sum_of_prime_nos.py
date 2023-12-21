'''
Answer to Question 1: Finding sum of prime numbers in a list of integers inputted by user
Write a program to read a list of integers from the user and print the sum of all the prime numbers in the list. 

Examples:

Input: [ 2, 10, 13, 5] should give output as 20
Input: [-2, 3, 0] should give output as 3
'''
myList = input('Enter a list of integers separated by space: ').split() # Taking a list of integers from user
for i in range(len(myList)):                                            # String to Int conversion of each integer
    myList[i] = int(myList[i])

sum = 0

'''
Below loops do following things:
1) Takes each element of inputted list one by one
2) Divide it with integers starting from 2 till that number
3) Number of times fully divisible will be 1 for a prime number
4) If integer is found to be a prime number, add it to sum

'''

for j in range(len(myList)):
    count = 0                                                           
    for k in range(2,myList[j]+1):
        if (myList[j]%k == 0):
            count += 1
    if (count == 1):
        sum += myList[j]

print('Sum of Prime numbers in the list = ',sum)
            
