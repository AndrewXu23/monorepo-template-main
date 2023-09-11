"""
 Sample modified from CS5500, Mike Shah

 A rectangle class
 Note that there is no constructor or destructor,
 so a default one will be created for us.
"""

from abc import ABC, abstractmethod
# ABC stands for "abstract base class." subclasses of ABC can declare abstract methods

class Shape(ABC):
    @abstractmethod
    def set_values(self, x, y):
        pass

    @abstractmethod
    def area(self):
        pass

class Rectangle:
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    def set_values(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def setWidth(self, width):
        self.width = width

    def setHeight(self, height):
        self.height = height

if __name__ == "__main__":
    # Create a rectangle object
    rect = Rectangle(3, 4)

    # Call a member function
    rect.set_values(3, 4)

    # Print out the area function
    print("area:", rect.area())
