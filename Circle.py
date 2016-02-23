import math 

class Circle:
    # Construct a circle object 
    def __init__(self, radius = 1):  ##  If we put nothing, there will be no default value
        self.radius = radius  ##  self is special parameter that represents the object inside the class

    def getPerimeter(self):
        return 2 * self.radius * math.pi

    def getArea(self):
        return self.radius * self.radius * math.pi
          
    def setRadius(self, radius):
        self.radius = radius