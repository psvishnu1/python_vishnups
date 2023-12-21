'''
Answer to Question number 4, week 01
Write a program which will take a list of numbers and produce a set which contains the prime factors of every number in the list.
'''

def prime_list_find(number):                                                                        # function to create a list of prime numbers upto a given number N 
    def is_prime(n):
        count = 0
        for i in range(2,n+1):
            if (n % i == 0):
                count=count+1
        if (count==1):
            return(True)
        else:
            return(False)

    for i in range(2,number+1):                                                      
        if (is_prime(i) == True):
            prime_list.append(i)


list_of_num = [int(item) for item in input("Enter the numbers separated by space: ").split()]       # Taking inputs from user
list_of_factors = []

for i in list_of_num:
    prime_list = []
    set_of_factors = set()
    prime_list_find(i)                                                                              # finding prime numbers upto given number
    for j in prime_list:                                                
        while ((i % j) == 0):                                                                       
            set_of_factors.add(j)                                                                   # add factor to a set of prime factors
            i = i/j
    list_of_factors.append(set_of_factors)                                                          # add set of prime factors to a list of factors

print('The respective prime factors of each number is : ', list_of_factors)                         # output




