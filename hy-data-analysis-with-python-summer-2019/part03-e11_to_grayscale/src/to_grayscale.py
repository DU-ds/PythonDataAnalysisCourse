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
    

def main():
    img = plt.imread("R:/Git/PythonDataAnalysisCourse/hy-data-analysis-with-python-summer-2019/part03-e11_to_grayscale/src/painting.png")
    # plt.imread("src/painting.png")
    plt.imshow(img)
    grey_img = to_grayscale(img)
    plt.imshow(grey_img)

    

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