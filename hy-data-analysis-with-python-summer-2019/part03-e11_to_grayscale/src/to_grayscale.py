#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

def to_grayscale(img):
    """3D array to 2D array
    
    Args:
        img: RGB image stored as red in matrix 1, 
        green in matrix 2, blue in matrix 3
    Returns:
        grey_img: matrix encoding greyscale version of img
    """
    red_weight = 0.2126
    green_weight = 0.7152
    blue_weight = 0.0722
    img2 = img.copy()
    img2[:,:,0] *= red_weight
    img2[:,:,1] *= green_weight
    img2[:,:,2] *= blue_weight
    return np.sum(img2, axis = 2)

def to_one_RGB(a, color):
    """
    assumes red is in axis 0, green is in axis 1, and blue is in axis 2
    """
    img = a.copy() # np arrays are mutable right?
    color = color.lower() #so a user can type Red, RED, ReD, rED, R, r and get a red img back
    if color == "red" or color == "r":
        other_colors = [1,2]
    elif color == "green" or color == "g":
        other_colors = [0,2]
    elif color == "blue" or color == "b":
        other_colors = [0,1]
    else:
        raise ValueError("not a valid color\nAccepts: red, green, and blue")
    
    img[:,:,other_colors] *= 0 #now only 1 of the 3 colors is non-zero.
    return img
    
    

def to_red(a):
   return to_one_RGB(a, "red")   

def to_green(a):
    return to_one_RGB(a, "green")

def to_blue(a):
    return to_one_RGB(a, "blue")
            

def main():
    f = "src/painting.png"
    # f = "hy-data-analysis-with-python-summer-2019/part03-e11_to_grayscale/src/painting.png"
    # f = "R:/Git/PythonDataAnalysisCourse/hy-data-analysis-with-python-summer-2019/part03-e11_to_grayscale/src/painting.png"
    ace = plt.imread(f)
    plt.imshow(ace)
    grey_ace = to_grayscale(ace)
    # plt.gray() # because it needs to print it as a black and white image
    plt.imshow(grey_ace, cmap = "gray")
    # plt.plot(grey_ace)
    
    # plt.
    pic, plots = plt.subplots(3,1)
    red = to_red(ace)[:,:,0]
    plots[0].imshow(red)
    # plots[0].imshow(red, cmap = "Reds")

    green = to_red(ace)[:,:,1]
    plots[1].imshow(green)
    # plots[0].imshow(green, cmap = "Greens")
    
    blue = to_red(ace)[:,:,2]
    plots[2].imshow(blue)
    # plots[0].imshow(blue, cmap = "Blues")
    # plots.show()
    

if __name__ == "__main__":
    main()

"""Use the weights 0.2126, 0.7152, and 0.0722 for red, green, and blue, respectively.
Part 1.

Write a function to_grayscale that takes an RGB image (three dimensional array) 
and returns a two dimensional gray-scale image. The conversion to gray-scale 
should take a weighted sum of the red, green, and blue values, and use that as 
the value of gray. The first axis is the x, the second is y, and the third is the 
color components (red, green, blue). Use the weights 0.2126, 0.7152, and 0.0722 
for red, green, and blue, respectively. These weights are so because the human 
eye is most sensitive to green color and least sensitive to blue color.

In the main function you can, for example, use the provided image src/painting.png. 
Display the grayscale image with the plt.imshow function. You may have to call the 
function plt.gray to set the color palette (colormap) to gray. (See help(plt.colormaps) 
for more information about colormaps.)
"""
