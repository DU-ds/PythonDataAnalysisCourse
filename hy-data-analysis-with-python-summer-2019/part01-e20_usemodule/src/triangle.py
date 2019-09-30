#!/usr/bin/env python3
""" triange math. Currently can be used to 
find the hypotenuse and area of a triangle.
"""
__author__ = "Du_ds"
__version__ = "1.0.0"
import math

def hypothenuse(a, b):
    """
    returns the length of the hypothenuse when given 
    the lengths of two other sides of a right-angled triangle
    a^2 + b^2 = c^2
    """
    c_squared = a**2 + b **2
    return math.sqrt(c_squared)

def area(a, b, theta = math.pi/2):
    """
    returns the area of the right-angled triangle using side angle side method

    Args:
        a: numeric
            length of side a,
        b: numeric
            length of side b, 
        theta: numeric
            angle between side a and side b
            in radians
            default is pi/2 ie 90 degrees
        """
    A = 1/2 * a * b * math.sin(theta)
    return A

