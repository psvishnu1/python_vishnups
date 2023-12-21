'''
Write a program which will request the user to enter two lists of real numbers (floats) of the same length and print the dot-product of the two lists.

	1) For example, if the two lists are [1.5, 0, 3.4] and [2.0, 3.1, 0] then the program should print 3.0

	2) The program should first ask the user to enter the length of the lists and then ask them to enter all elements of the first list one by one and then the second list one by one.

	3) The program should use only a basic loop (for or while) and not any advanced library functions.

'''

list1_length = int(input('Enter length of list 1: '))
list2_length = int(input('Enter length of list 2: '))
list_1 = []
list_2 = []
list_3 = []
if (list1_length != list2_length):
    print('List lengths are not the same')
else:
    for i in range(list1_length):
        list_1.append(float(input('Enter a number to add to list 1: ')))
    for j in range(list2_length):
        list_2.append(float(input('Enter a number to add to list 2: ')))

    for i in range(list1_length):
        list_3.append(list_1[i]*list_2[i])

    print ('Dot product of given lists is: ', list_3)
