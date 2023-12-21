'''
Answer to Question 6; week01
Design a class Student suited to capture the required details of a student enrolled to a course cs5017. 
The Student class should at least contain basic information like roll number (int), full name (str), program name (str), whether the student has prior programming experience (boolean), etc. 
It should also be able to store the marks of three tests. You can add more based on your imagination.

Design a class course which can store a list of students and some extra information like maximum strength allowed, average of test-1, average of test-2, etc. 
Write methods to compute these averages. Also add methods to:

1) add a new student (it should permit this only if the strength is within limits)
2) search for a student by roll number
3) search for a student by a part of her name
4) print the student data in a very readable format (like a spreadsheet)
5) modify the above method so that you can print the list sorted by either roll number or name.
'''
class student:                                                                                                  # class for holding individual student data
    def __init__(self):
        self.roll_no = int(input('Enter roll number: '))
        self.name = input('Enter full name:')
        self.prog_name = input('Enter Program name: ')
        self.prev_exp = bool(input('Previous experience True/False: '))
        self.marks = [int(item) for item in input('Enter marks for 3 tests separated by space: ').split()]

    def print_std(self):                                                                                        # function to print individual student data
        print('Student name: ',self.name)
        print('Roll number: ',self.roll_no)
        print('Program: ',self.prog_name)
        print('Previous Experience: ',str(self.prev_exp))
        print('Marks in 3 tests respectively: ',self.marks)

class course:                                                                                                   # class for holding cs5107 course data
    def __init__(self,max_stdnt):
        self.registered_std = []
        self.max_cap = max_stdnt

    def add_std(self,stdnt1):                                                                                   # funtion to add students to course cs5107
        if(len(self.registered_std)<self.max_cap):
            self.registered_std.append(stdnt1)
        else:
            print("Cannot add, Max capacity reached")
    
    def find_avg(self):                                                                                         # function to find average marks of tests
        self.sum_1 = 0
        self.sum_2 = 0
        for i in range(0,len(self.registered_std)):
            self.sum_1+=self.registered_std[i].marks[0]
            self.sum_2+=self.registered_std[i].marks[1]
            self.avg_1 = self.sum_1/len(self.registered_std)
            self.avg_2 = self.sum_2/len(self.registered_std)
        print('Average marks for test 1 = ',self.avg_1)
        print('Average marks for test 2 = ',self.avg_2)

    def search_std(self):                                                                                       # function to search for students
        self.user_inp = input("Enter 'roll' for searching by Roll number and 'name' for name based search: ")
        self.found = 0
        if(self.user_inp == 'roll'):                                                                            # search based on roll number
            self.search_roll = int(input("Enter student's roll number: "))
            for i in range(0,len(self.registered_std)):
                if(self.registered_std[i].roll_no == self.search_roll):
                    print('Student found')
                    stdnt[i].print_std()
                    self.found = 1
            if(self.found == 0):
                print("No student with given roll number")
            
        elif(self.user_inp == 'name'):                                                                          # search based on name
            self.search_name = input("Enter student's name: ")
            for i in range(0,len(self.registered_std)):
                if(self.search_name in self.registered_std[i].name):
                    print('Student found')
                    stdnt[i].print_std()
                    self.found = 1
            if(self.found == 0):
                print("No student having given name")

        else:
            print('Wrong Input')

    def print_data(self):                                                                                       # function to print entire student data in table format
        self.user_inp_3 = input("Enter 'roll/name' to print sorted that way:")
        if(self.user_inp_3 == 'roll'):
            self.sorted_list = sorted(self.registered_std, key=lambda e:e.roll_no)
            print("{:<8} {:<15} {:<10} {:<10} {:<10} {:<10}".format('Name','Roll No','Prog.Name','Prev.Exp','Test 1 Marks', 'Test 2 Marks'))
            for i in range(0,len(self.sorted_list)):
                print ("{:<8} {:<17} {:<12} {:<9} {:<14} {:<14}".format(self.sorted_list[i].name, self.sorted_list[i].roll_no, self.sorted_list[i].prog_name, str(self.sorted_list[i].prev_exp),self.sorted_list[i].marks[0],self.sorted_list[i].marks[1]))

        elif(self.user_inp_3 == 'name'):
            self.sorted_list = sorted(self.registered_std, key=lambda e:e.name)
            print("{:<8} {:<15} {:<10} {:<10} {:<10} {:<10}".format('Name','Roll No','Prog.Name','Prev.Exp','Test 1 Marks', 'Test 2 Marks'))
            for i in range(0,len(self.sorted_list)):
                print ("{:<8} {:<17} {:<12} {:<9} {:<14} {:<14}".format(self.sorted_list[i].name, self.sorted_list[i].roll_no, self.sorted_list[i].prog_name, str(self.sorted_list[i].prev_exp),self.sorted_list[i].marks[0],self.sorted_list[i].marks[1]))

        else:
            print('Wrong Input')


stdnt = []

no_of_stdnts = int(input('Enter number of students in general: '))                                              # program initial value setting
for i in range(0,no_of_stdnts):
    stdnt.append(student())

course_stdnts = int(input('Enter max number of students for course cs5107: '))
cs5107 = course(course_stdnts)
for i in range(0,no_of_stdnts):
    cs5107.add_std(stdnt[i])


while(input("Do you wish to end program, yes/no :") == 'no'):                                                   # switching between functions based on user inputs
    while (input('Do you wish to add more students to course cs5107, yes/no : ') == 'yes'):
        stdnt.append(student())
        cs5107.add_std(stdnt[-1])
    while(input('Do you wish to search for a student, yes/no : ') == 'yes'):
        cs5107.search_std()
    if(input('Do you wish to find average marks of the tests, yes/no: ') == 'yes'):
        cs5107.find_avg()
    elif(input('Do you wish to print the entire student data, yes/no : ') == 'yes'):
        cs5107.print_data()
    else:
        print("Wrong Input")     
