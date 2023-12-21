'''
Enhance the Reel class from previous lab with the following methods.

1) draw(self,canvas,xcenter,ycenter) which will draw the first polygon in the reel on the canvas that is passed to it with center at (xcenter, ycenter). 
It should also have a previous and next buttun to cycle through the different polygons in the reel.
'''

import math
import tkinter as tk

class Polygon:                                                                                          # Polygon class mentioned in question
    def __init__(self, sides, length):
        self.sides = sides
        self.length = length

    def perimeter(self):
        return self.sides * self.length

    def area(self):
        theta = math.pi/self.sides
        inRadius = (self.length/2) / math.tan(theta)
        area = self.sides * (0.5 * self.length * inRadius)
        return(area) 

    def info(self):
        print(f'Polygon with {self.sides} sides')
        print('Side length:', self.length)
        print('Perimeter:', self.perimeter())


class Reel:                                                                                             # Reel class mentioned in question
    def __init__(self, area):
        self.areaLimit = area
        self.polygons = []
        self.count = 0

    def info(self):
        print('The list of following Polygons')
        for p in self.polygons:
            p.info()

    def addPolygon(self, newPolygon):
        totalArea = 0
        for p in self.polygons:
            totalArea += p.area()
        totalArea += newPolygon.area()
        if totalArea <= self.areaLimit:
            self.polygons.append(newPolygon)
        else:
            print('Area Limit of Reel Exceeded. Polygon not added')


    def getCoordinates(self, xcenter, ycenter,cnt):
        self.crd = []
        self.theta = (2*math.pi)/self.polygons[cnt].sides                                               # finding angle between center and line joining 2 adjacent corners for given polygon
        self.cirRadius = ((self.polygons[cnt].length)/(2*math.sin(math.pi/self.polygons[cnt].sides)))   # finding circumradius for given polygon
        for i in range(0,self.polygons[cnt].sides):
            self.xx = xcenter + (self.cirRadius*math.cos(i*self.theta))                                 # finding co-ordinates of each i'th corner and appending it to a list
            self.yy = ycenter + (self.cirRadius*math.sin(i*self.theta))
            self.crd.append(self.xx)
            self.crd.append(self.yy)
        return(self.crd)

    def draw(self,canvas,xcenter,ycenter):
        allCoord = self.getCoordinates(xcenter,ycenter,self.count)                                      # calls function to find co-ords of present polygon
        self.drawed_polygon = myCanvas.create_polygon(allCoord,fill='blue')                             # draws present polygon in canvas
    

listOfPolygons = [Polygon(4,100), Polygon(5,200), Polygon(3,250), Polygon(6,150)]                                                       # Polygon list user provided
reel = Reel(1000000.0)                                                                                  # Max area user provided

center_Coord = [400,300]                                                                                # Center co-ordinates of polygon user provided
x = 800
y = 600

for p in listOfPolygons:
    p.info()
    print('Area:', p.area())
    reel.addPolygon(p)

def nextAction():                                                                                       # action performed when next button pressed
    if(reel.count<(len(reel.polygons)-1)):
        myCanvas.delete(reel.drawed_polygon)
        reel.count+=1
        reel.draw(myCanvas,center_Coord[0],center_Coord[1])

def prevAction():                                                                                       # action performed when prev button pressed
    if(reel.count>0):
        myCanvas.delete(reel.drawed_polygon)
        reel.count-=1
        reel.draw(myCanvas,center_Coord[0],center_Coord[1])

window = tk.Tk()
window.geometry('1600x1200')
window.title('My Polygon')
heading = tk.Label(window,text='Below is my drawing wall',font=('Times',32))                            #characterising a label
heading.pack()
myCanvas = tk.Canvas(window,width = x, height = y, background = 'green')
myCanvas.pack(pady=100)
myCanvas.create_line(0,y/2,x,y/2)
myCanvas.create_line(x/2,0,x/2,y)
reel.draw(myCanvas,center_Coord[0],center_Coord[1])
prevBtn = tk.Button(window,text = 'PREV',command=prevAction, background='red',font=('Times',32))  #characterising a button
prevBtn.pack()
nextBtn = tk.Button(window,text = 'NEXT',command=nextAction, background='red',font=('Times',32))  #characterising a button
nextBtn.pack()
window.mainloop()
