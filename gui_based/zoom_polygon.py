'''
Answer to Home Excercise 1
Add two buttons zoom-in and zoom-out to the window so that clicking on them will respectively enlarge or shrink the polygon by 1.5 times.
'''

import tkinter as tk
import math

class Polygon():
    def __init__(self, sides, length):
        self.sides = sides
        self.length = length

    def perimeter(self):
        return self.sides * self.length

    def info(self):
        print(f'Polygon with {self.sides} sides')
        print('Side length:', self.length)
        print('Perimeter:', self.perimeter())
    
    def getCoordinates(self, xcenter, ycenter):
        self.crd = []
        self.theta = (2*math.pi)/self.sides                                         # finding angle between center and line joining 2 adjacent corners for given polygon
        self.cirRadius = ((self.length)/(2*math.sin(math.pi/self.sides)))           # finding circumradius for given polygon
        for i in range(0,self.sides):
            self.xx = xcenter + (self.cirRadius*math.cos(i*self.theta))              # finding co-ordinates of each i'th corner and appending it to a list
            self.yy = ycenter + (self.cirRadius*math.sin(i*self.theta))
            self.crd.append(self.xx)
            self.crd.append(self.yy)
        return(self.crd)


    def draw(self,canvas,co_ord):
        self.drawed_polygon = myCanvas.create_polygon(co_ord,fill='blue')                                 # function to draw polygon with given co-ordinates



no_of_sides = int(input('Enter number of sides of polygon: '))
length_of_side = int(input('Enter length of each side: '))
p = Polygon(no_of_sides,length_of_side)

def nextAction():                                                                   # clear button action definition
    print("Pressed clear button")
    myCanvas.delete(p.drawed_polygon)

def zm_in():
    myCanvas.scale(p.drawed_polygon,xctr,yctr,1.5,1.5)

def zm_out():
    myCanvas.scale(p.drawed_polygon,xctr,yctr,0.5,0.5)

x = 800
y = 600
center = []

xctr = int(input('Enter X co-ordinate of center: '))
center.append(xctr)
yctr = int(input('Enter y co-ordinate of center: '))
center.append(yctr)

allCoord = p.getCoordinates(center[0],center[1])
print(allCoord)

window = tk.Tk()
window.geometry('1600x1200')
window.title('My Polygon')
heading = tk.Label(window,text='Below is my drawing wall',font=('Times',32))                        #characterising a label
heading.pack()
myCanvas = tk.Canvas(window,width = x, height = y, background = 'green')
myCanvas.pack(pady=100)
myCanvas.create_line(0,y/2,x,y/2)
myCanvas.create_line(x/2,0,x/2,y)
p.draw(myCanvas,allCoord)
zoomInBtn = tk.Button(window,text = 'Zoom-In',command=zm_in, background='cyan',font=('Times',32))  #characterising a button
zoomInBtn.pack(side='left')
zoomOutBtn = tk.Button(window,text = 'Zoom-Out',command=zm_out, background='cyan',font=('Times',32))  #characterising a button
zoomOutBtn.pack(side='right')
clearBtn = tk.Button(window,text = 'CLEAR',command=nextAction, background='red',font=('Times',28))  #characterising a button
clearBtn.pack()
window.mainloop()
