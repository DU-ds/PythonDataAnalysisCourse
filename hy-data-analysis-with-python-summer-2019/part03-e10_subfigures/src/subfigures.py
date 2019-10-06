#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

def subfigures(a):
    pic, plts = plt.subplots(1,2)
    plts[0].plot(a[:,0], a[:,1])
    plts[0].set_title("CYMK axis labels")
    plts[0].set_xlabel("Cyan", color = "c")
    plts[0].set_ylabel("Yellow", color = "y")
    plts[1].scatter(a[:,0], a[:,1], c = a[:,2], s = a[:,3])
    plts[1].set_xlabel("Magenta", color = "m")
    plts[1].set_ylabel("Black", color = "k")
    plt.show()

def main():
    ace = np.array([[1,24,7,10],[12/5,15/7, 51/6,12/4],[0.79,0.45,0.85,0.27], [12,12,12,12]])
    grey_ace = subfigures(a)
    

if __name__ == "__main__":
    main()
