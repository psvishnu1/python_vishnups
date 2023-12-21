'''
	Question: Add the following methods to the polygon class:
			1) outRadius() which gives the radius of the circumcircle of the polygon
			2) inRadius() which gives the radius of the incircle of the polygon
				Override the calcArea methods in the inherited class Square. 
'''

from cmath import pi
import math

class polygon:                                                                      #general class for all regular polygons
    def __init__(self,side,len):                                                    #class initialization
        self.sides = side
        self.length = len

    def calcArea(self):                                                             #Function to find area of regular polygon
        self.area = ((self.length ** 2)*self.sides)/(4*math.tan(pi/self.sides))
        return(self.area)

    def outRadius(self):                                                            #Function to find Circum radius of regular polygon
        self.outrad = ((self.length)/(2*math.sin(pi/self.sides)))
        return(self.outrad)

    def inRadius(self):                                                             #Function to find Inradius of regular polygon
        self.inrad = ((self.length)/(2*math.tan(pi/self.sides)))
        return(self.inrad)


class square(polygon):                                                              #special class for square, inherited from polygon class
    def __init__(self,side,len):                                                    #class initialization
        self.sides = side
        self.length = len

    def calcArea(self):                                                             #Function to find area of square which overrides function of same name in parent class
        print('Successfuly overrided parent function')
        self.area = self.length ** 2
        return(self.area)
        
N = int(input('Enter number of sides of regular polygon: '))                        #Taking inputs from user
L = int(input('Enter length of each side of regular polygon: '))

if (N == 4):                                                                        #if condition to make sure appropriate class based on inputs are selected
    obj = square(4,L)
    print('Area of Polygon = ', obj.calcArea())
    print('Circumradius of Polygon = ', obj.outRadius())
    print('Inradius of Polygon = ', obj.inRadius())
else:
    obj = polygon(N,L)
    print('Area of Polygon = ', obj.calcArea())
    print('Circumradius of Polygon = ', obj.outRadius())
    print('Inradius of Polygon = ', obj.inRadius())
