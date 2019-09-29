#!/usr/bin/env python3

import math


def main():
    
    while True:
        s = input("Choose a shape (triangle, rectangle, circle): ")
        if(s == "triangle" or s == "Triangle"):
            base = float(input("Give base of the triangle: "))
            height = float(input("Give height of the triangle: "))
            area = 0.5 * base * height
            print("The area is %s" % area )
        elif s == "rectangle" or s == "Rectangle":
            width = float(input("Give width of the rectangle: "))
            height = float(input("Give height of the rectangle: "))
            area = width * height
            print("The area is %f" % area)
        elif s == "circle" or s == "Circle":
            radius = float(input("Give radius of the circle: "))    
            area = math.pi * radius**2
            print("The area is %f" % area)
        elif s == "":
            break
        else:
            print("Unknown shape!")


if __name__ == "__main__":
    main()
