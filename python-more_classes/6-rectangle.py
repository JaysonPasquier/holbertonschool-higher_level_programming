#!/usr/bin/python3
'''
Module for Class Rectangle
'''


class Rectangle:
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        '''Initialization method for Rectangle'''
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        '''Getter method for width attribute'''
        return self.__width

    @width.setter
    def width(self, value):
        '''Setter method for width attribute'''
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        '''Getter method for height attribute'''
        return self.__height

    @height.setter
    def height(self, value):
        '''Setter method for height attribute'''
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        '''Method to calculate area of the rectangle'''
        return self.__width * self.__height

    def perimeter(self):
        '''Method to calculate perimeter of the rectangle'''
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        '''Method to return string representation of the rectangle'''
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join(["#" * self.__width for _ in range(self.__height)])

    def __repr__(self):
        '''Method to return formal string representation of the rectangle'''
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        '''Method to print message when an instance is deleted'''
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
