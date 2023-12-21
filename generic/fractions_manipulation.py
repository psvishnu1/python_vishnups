'''
Create a class called Fraction that can store a fraction of the form a/b where b is non-zero. This class should support the following methods:

	1) disp() -- this function takes no argument and displays the fraction in the form a/b.

	2) addInt() -- this function takes an integer as argument and adds it to itself.

	3) addFrac() -- this function takes another object of class fraction and adds it to itself.

	4) multFrac() -- this function takes another object of class fraction and multiplies it to itself.

	5) simplify() -- this function takes no argument and removes any common factors from numerator and denominator.

Note that the constructor for the class (__init__) should fail if the denominator is 0.
'''

class Fraction:
    def __init__(self,a,b):
        self.a = a
        if(b != 0):
            self.b = b
        else:
            print('Denominator cannot be zero!')
            return

    def disp(self):
        self.myFraction = str(self.a)+'/'+str(self.b)
        print('My fraction is: ', self.myFraction)

    def addInt(self,num):
        newNum = self.a + (self.b * num)
        self.a = newNum

    def addFrac(self,ob2):
        newNum = (self.a * ob2.b) + (self.b * ob2.a)
        newDen = self.b * ob2.b
        self.a = newNum
        self.b = newDen

    def multFrac(self,ob2):
        newNum = self.a * ob2.a
        newDen = self.b * ob2.b
        self.a = newNum
        self.b = newDen

    def simplify(self):
        if(self.a < self.b):
            smallest = self.a
        else:
            smallest = self.b
        i = 2
        while (i < smallest+1):
            while (self.a % i == 0 and self.b % i == 0):
                self.a = int(self.a / i)
                self.b = int(self.b / i)
            i += 1
                       
p = Fraction(32,4)
q = Fraction(1,2)

# p.addInt(1)
# p.disp()

# p.addFrac(q)
# p.disp()

# p.multFrac(q)
# p.disp()

# p.disp()
p.simplify()
p.disp()
