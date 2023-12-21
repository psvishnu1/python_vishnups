'''
Answer to Question number 3, week 01
Write a method inside the class Reel that will print the polygons in a reel in the increasing order of their area.
'''

from cmath import pi
import math

class Reel:
    def __init__(self,number_of_polygons):                                                      # Function to get polygon input from user                                                     
        
        for i in range(1,number_of_polygons+1):
            no_of_sides = int(input(f'Enter number of sides of the polygon {i} = '))
            if(no_of_sides < 3):
                print('Not a Polygon')
                continue
            side_length = int(input(f'Enter the length of sides of the polygon {i} = '))
            area = round(((side_length ** 2)*no_of_sides)/(4*math.tan(pi/no_of_sides)))
            list_of_polygons.append([f'Polygon {i}',area])                                      # Creates a 2D list of polygons and their respective areas
        
    def Polygon_print(self):
        polygon_sorted = sorted(list_of_polygons, key=lambda e:e[1])                            # Polygon list sorted based on 2nd element
        print('Polygon list before sorting: ', list_of_polygons)
        print('Polygon list after sorting based on area: ', polygon_sorted)

list_of_polygons = []
number_of_polygons = int(input("Total number of polygons = "))
object_of_reel = Reel(number_of_polygons)
object_of_reel.Polygon_print()
