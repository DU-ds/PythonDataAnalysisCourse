#!/usr/bin/env python3
import os
import math
import numpy as np
import matplotlib.pyplot as plt


def center(a):
    nrows, ncols = a.shape[:2]
    nrows -= 1
    ncols -= 1
    return (nrows/2,ncols/2)   # note the order: (center_y, center_x)

def radial_distance(a):
    nrows, ncols = a.shape[:2]
    center_x, center_y = center(a)
    G = ( (((x - center_x)**2 + (y - center_y)**2)**(1/2))
         for x in range(nrows)
         for y in range(ncols))
    return np.array(list(G)).reshape(nrows,ncols)
    # return np.array([(x, y) for r in G]) # create teh 2d array. 

def scale(a, tmin=0.0, tmax=1.0):
    """Returns a copy of array 'a' with its values 
    scaled to be in the range [tmin,tmax].
    
    output.min() = tmin
    output.max = tmax
    
    Note: Does not work for constant arrays unless tmin == tmax
    not otherwise possible!
    returns array set to tmax
    
    Also, if setting min to tmin makes max zero, sets to max then returns
    """
    a2 = a.astype(float, casting = "unsafe") #needs a float array to scale
    if a2.min() == tmin:
        pass #min is already tmin
    elif a2.min() > tmin:
        offset = a2.min() - tmin # set min to tmin
        a2 -= offset 
    elif a2.min() >= 0: # < tmin, >= 0
        offset = tmin - a2.min()
        a2 += offset
    else:
        offset = math.fabs(a2.min()) # min will be zero
        offset += tmin # min will now be tmin
        a2 += offset
    if tmax == a2.max():
        pass
    elif a2.max() == 0:
        return a2 + a2.max() # hack cause max should not be zero
    a2 /= a2.max() # normalize the array
    a2 *= tmax  # scale to have max
    return a2

def radial_mask(a):
    a2 = a.astype(float, casting = "unsafe")
    a2 = radial_distance(a2)
    a2 = scale(a2)
    a2 = 1 - a2
    return a2

def radial_fade(a):
    mask = radial_mask(a)
    return a * mask[:,:,np.newaxis] # 2d array to 3d array to allow broadcasting

def main():
    # f = os.getcwd() + "/painting.png"
    f = os.path.dirname(os.path.realpath(__file__)) + "/painting.png"
    # f = "/src/painting.png"
    img = plt.imread(f)
    fig, plots = plt.subplots(3,1)
    plots[0].imshow(img)
    mask = radial_mask(img)
    plots[1].imshow(mask)
    faded = radial_fade(img)
    plots[2].imshow(faded)
    plt.show()

if __name__ == "__main__":
    main()
