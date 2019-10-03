#!/usr/bin/env python3

import numpy as np

def diamond(n):
    def dims(n):
        return 2 * n - 1
    nxn = dims(n) 
    base = np.eye(nxn)
    bottom_left = base[0:n,0:n]
    # will be bottom left of result. right side will have dims one less than left
    bottom_right = base[n-1:, n:]
    bn = bottom_right.shape[0]
    lst_br = []
    for i in range(0, bn): 
    # reverse the ordering since the rows of bottom right are in the wrong order
        i2 = bn -1 - i
        lst_br.append(bottom_right[i2,:])
    # now put them in a np array
    bottom_right = np.array(lst_br)
    top_left = base[bn:bn + (bn+1)//2, (bn+1)//2: bn + (bn )//2]
    bottom_right[:(bn+1)//2, :]
    lst_tl = []
    for i in range(top_left.shape[0]):
        i2 = top_left.shape[0] - 1 - i
        lst_tl.append(top_left[i2,:])
    top_left = np.array(lst_tl)
    # since bn is odd, // == / but gives an int 
    # selecting the upper left square, since diamonds are symetric
    top_right = bottom_left[0:(bn+1)//2,:bn]
    top = np.concatenate((top_left, top_right), axis = 1)
    bottom = np.concatenate((bottom_left, bottom_right), axis = 1)
    #putting left and right side by side
    result = np.concatenate((top, bottom), axis = 0)
    return result

def main():
    print("\n", diamond(3))

if __name__ == "__main__":
    main()

# pattern of input to diamond to output array size 
# f(n) = 2n -1 
# 1 : 1
# 2 : 3
# 3 : 5
# 4 : 7