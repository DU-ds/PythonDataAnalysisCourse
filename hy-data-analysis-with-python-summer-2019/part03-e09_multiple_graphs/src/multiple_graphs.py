#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np

def main():
    x1 = np.array([2,4,6,7])
    y1 = np.array([4,3,5,1])
    plt.plot(x1, y1)
    
    x2 = np.array([1,2,3,4])
    y2 = np.array([4,2,3,1])
    plt.plot( x2, y2)
    plt.xlabel("x")
    plt.ylabel("y")
    
    plt.title("Exercise 9 (multiple graphs)")
    plt.show()


if __name__ == "__main__":
    main()

"""
Make your main function plot the following two graphs in one axes. 
The first graphs has x coordinates 2,4,6,7 and y coordinates 4,3,5,1. 
The second graph has x coordinates 1,2,3,4 and y coordinates 4,2,3,1.

Add also a title and some labels for x axis and y axis. 
Note that in the non-interactive mode you have to call plt.show() 
=hfor the figure to show.
"""

