'''
Answer to Question number 3, week 01
Write popSmall and popBig methods to the class Reel which will respectively remove and return the smallest and biggest (in terms of area) polygon in the reel.
'''
from cmath import pi
import math

list_of_polygons = []                                                                               # 2D List of polygons

class Reel:
    def popSmall(self):                                                                             # Module for popping smallest area polygon
        list_of_polygons_2 = sorted(list_of_polygons, key=lambda e:e[2], reverse = True)
        removed_polygon = list_of_polygons_2.pop()
        return(removed_polygon)

    def popBig(self):                                                                               # Module for popping biggest area polygon
        list_of_polygons_2 = sorted(list_of_polygons, key=lambda e:e[2])
        removed_polygon = list_of_polygons_2.pop()
        return(removed_polygon)

object_of_reel = Reel()                                                                             # class instantiation
number_of_polygons = int(input("Total number of polygons = "))

for i in range(1,number_of_polygons+1):                                                             # appending user inputs to list of polygons
    no_of_sides = int(input(f'Enter number of sides of the polygon {i} = '))
    if(no_of_sides < 3):
        print("Not a polygon")
        continue
    side_length = int(input(f'Enter the length of sides of the polygon {i} = '))
    area = ((side_length ** 2)*no_of_sides)/(4*math.tan(pi/no_of_sides))
    list_of_polygons.append([no_of_sides,side_length,area])

small_or_big = input("Enter 'small' or 'big' based on polygon to be popped = ")

if(small_or_big == 'big'):                                                                          # Checking of action required on list
    popped_polygon = object_of_reel.popBig()
elif(small_or_big == 'small'):
    popped_polygon = object_of_reel.popSmall()
else:
    print('Wrong Input')

print(f"List of Polygons before popping in 'Sides', 'Length', 'Area' format = {list_of_polygons}")
print(f"Polygon which was popped out = {popped_polygon }")
