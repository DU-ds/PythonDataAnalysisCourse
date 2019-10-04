#!/usr/bin/env python3

import numpy as np
import scipy.linalg

def vector_angles(X, Y):
    x_dot_y = np.sum(X * Y, axis = 1)
    x_dot_x = np.sum(X * X, axis = 1)
    y_dot_y = np.sum(Y * Y, axis = 1)
    cos_xy = x_dot_y/(np.sqrt(y_dot_y) * np.sqrt(x_dot_x))
    cos_xy = np.clip(cos_xy, a_min = -1, a_max = 1)
    return np.arccos(cos_xy)

# https://docs.scipy.org/doc/numpy/reference/generated/numpy.einsum.html#numpy.einsum

def main():
    X = numpy.arange(12).reshape(3,4)
    Y =  2 * numpy.random.randint(0, 12, size = (3, 4))
    angle = vector_angles(X, Y)
    print(angle)

if __name__ == "__main__":
    main()
