'''
In this question we want to create a class PlotSin to plot the graph of sin(x) for x in the range -2pi to 2pi using tkinter and canvas.

	1) Create a PlotSin class does the following when created

	2) Creates a window and a canvas object.

	3) Then, draw the x and y axes on canvas.

	4) Plots the graph of sin(x) for x in the range -2pi to +2pi

	5) Ensure that the axes are scaled so that the plot fills the canvas.

Hint You can plot a dot at a point using tkinter's create_line() function itself
'''

from numbers import Real
import tkinter as tk
import math

class PlotSin:

    '''
    If we need 2 cycles in given width, let's say given width = 400 pixels; then 400 pixels = 4*pi (one cycle is 2pi).
    Therefore 1 pixel = 4*pi / 400 -> scaling factor for x axis
    ScalingYFactor maps y in y=sin(x) value to given pixel system. Let's say peak of sin should appear at Y pixel = 75; then for y=sin(x)=1 -> net Y = y*75
    '''

    width = 1200                                         # width of canvas as well as window
    height = 800                                        # height of canvas as well as window
    noCycles = 4                                        # Number of cycles to be accomodated in given canvas
    frequency = 50                                      # Frequency of sin wave in Hertz
    TimePeriod = 1 / frequency                         # Timeperiod of sin wave
    stdpower = {3:'ms',6:'us',9:'ns',12:'ps'}
    count = 0
    while (TimePeriod < 1 or count not in stdpower):
        TimePeriod = TimePeriod * 10
        count += 1
    TimePeriod = int(TimePeriod)
    print(f'Timeperiod is {TimePeriod} {stdpower[count]}')
    scalingXFactor = (noCycles*2*math.pi)/width         # Scaling X axis as per given data
    scalingYFactor = height/4                           # Scaling Y axis as per given data, Max amplitude in this case = 300/4 = 75 when sin(x) = 1
    coordMatrix = []                                    # List for multiple x values and corresponding y=sin(x) values appended back to back

    def __init__(self):                                 # initializes Tkinter GUI window
        self.myWindow = tk.Tk()
        self.myWindow.geometry(str(self.width)+'x'+str(self.height))
        self.myWindow.title('Sin Plotter')
        self.myCanvas = tk.Canvas(self.myWindow, width = self.width, height = self.height, background = 'Green')
        self.myCanvas.pack()
        self.myCanvas.create_line(0,self.height/2,self.width,self.height/2)         # draws x axis
        self.myCanvas.create_line(self.width/2,0,self.width/2,self.height)          # draws y axis

    def run(self):
        self.myWindow.mainloop()                                                    # function to bring window alive
        

    def draw(self):

        '''
        Let number of cycles be 1. When i = -self.width; x in sin(x) will be -> -width * 2pi /width == -2pi
        Similarily when i = +self.width; x in sin(x) will be -> width * 2pi / width == 2pi
        so, here x is varying between (-2pi,2pi)
        ''' 

        for i in range(0,self.width,1):
            y = (math.sin(i*self.scalingXFactor)*-self.scalingYFactor)+(self.height/2)
            self.coordMatrix.append(i)
            self.coordMatrix.append(y)

        self.myCanvas.create_line(self.coordMatrix,fill='blue',width=10)

        for i in range(0,self.width,int(self.width/(2*self.noCycles))):
            axisShift = (self.TimePeriod * self.noCycles)/2
            xAxis = i*((self.TimePeriod*self.noCycles)/self.width)-axisShift
            print(xAxis)
            self.myCanvas.create_text(i,self.height/2,text=int(xAxis),fill="black", font=('Helvetica 20 bold'))

        for j in range(self.height,0,-50):
            yAxis = int((self.height/2)-j)
            self.myCanvas.create_text(self.width/2,j,text=yAxis,fill="black", font=('Helvetica 20 bold'))
           

p = PlotSin()
p.draw()
p.run()



