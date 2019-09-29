#!/usr/bin/env python3

import math

def solve_quadratic(a, b, c):
    discriminant = (b*b - 4 * a * c)
    if discriminant < 0:
        x1 = "complex number"
    else:
        x1 = -1 * b + math.sqrt(discriminant)
        x1 /= 2*a
    if discriminant < 0:
        x2 = "complex number"
    else:
        x2 =  -1 * b - math.sqrt(discriminant)
        x2 /= 2*a
    return (x1, x2)

def main():
    print(solve_quadratic(1, -2, 5))

if __name__ == "__main__":
    main()
