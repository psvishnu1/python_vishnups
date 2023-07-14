number = input('Enter a Positive Integer:')
number = int(number)

def isPowerOfTwo(number):
	while((number % 2 == 0) and (number != 0)):
		number = number/2
	if (number == 1):
		print('Yes')
	else:
		print('No')
	
isPowerOfTwo(number)
