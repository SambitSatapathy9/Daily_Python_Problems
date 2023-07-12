#Problem 15
# Write a python program to create a class called Point with attributes x and y. Write a method to calculate the distance between two points.

import math
class Point(object):
    
    def __init__(self,x,y):
        self.x = x
        self.y = y
        
    def distance(self,other_point):
        distancee = math.sqrt((self.x-other_point.x)**2+(self.y-other_point.y)**2)
        return distancee
    
point1 = Point(3,4)
point2 = Point(5,7)

print(point1.distance(point2))
