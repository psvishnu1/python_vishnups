'''
Write a program which will request the user to enter three integers and then print back the integer whose value is in the middle.

For example, if the user enters 3, 8, 5, the program should print 5

If any two integers entered are the same, then the program should print an error message Please enter three distinct integers

The program should use only basic if-elif-else checks and not advanced things like sort().
'''

print('Enter 3 integers:')
num1 = input('Enter number 1: ')
num2 = input('Enter number 2: ')
num3 = input('Enter number 3: ')

if (num1 == num2 or num1 == num3):
    print('Please Enter distinct numbers')
else:
    if(num2 > num1):
        if(num3>num2):
            middle = num2
        elif(num3>num1):
            middle = num3
        else:
            middle = num1

    else:
        if(num3>num1):
            middle = num1
        elif(num3<num2):
            middle = num2
        else:
            middle = num3
    
    print('Middle value is: ', middle)    





