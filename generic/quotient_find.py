'''
Write a function getIntegerPart() that takes two integers a and b and returns the quotient when a is divided by b. Do this without importing math library.
'''

def getIntegerPart():
    num1 = int(input('Enter number a: '))
    num2 = int(input('Enter number b: '))

    return(num1//num2)

print('Quotient on dividing a by b is: ', getIntegerPart())
