#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

def center(a):
    nrows, ncols = a.shape[:2]
    return (nrows/2,ncols/2)   # note the order: (center_y, center_x)

def radial_distance(a):
    nrows, ncols = a.shape[:2]
    center_x, center_y = center(a)
    G = ( ((x - center_x)**2 + (y - center_y)**2)**(1/2) 
         for x in range(nrows)
         for y in range(ncols))
    return np.array([(x, y) for r in ]) # create teh 2d array. 

def scale(a, tmin=0.0, tmax=1.0):
    """Returns a copy of array 'a' with its values scaled to be in the range
[tmin,tmax]."""
    return np.array([[]])

def radial_mask(a):
    return np.array([[]])

def radial_fade(a):
    return np.array([[]])

def main():
    pass

if __name__ == "__main__":
    main()
