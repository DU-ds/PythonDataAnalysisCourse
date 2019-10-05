#!/usr/bin/python3

import numpy as np

def meeting_planes(a1, b1, c1, a2, b2, c2, a3, b3, c3):
    A = np.array([[a1,b1,1],[a2,b2,1],[a3,b3,1]])
    b = np.array([-c1,-c2,-c3])
    x, y, z = np.linalg.solve(A, b)
    return (x,y,-1*z)
"""
|z1 = a1x + b1y + c1|   --> |-c1 = a1x + b1y - z1|      |-c1 = a1 + b1 - 1| |x|      |-c1 = a1 + b1 + 1| | x|  
|z2 = a2x + b2y + c2|   --> |-c2 = a2x + b2y - z2|  --> |-c2 = a2 + b2 - 1| |y|  --> |-c2 = a2 + b2 + 1| | y|   
|z3 = a3x + b3y + c3|   --> |-c3 = a3x + b3y - z3|      |-c3 = a3 + b3 - 1| |z|      |-c3 = a3 + b3 + 1| |-z|  



"""
def main():
    a1=1
    b1=4
    c1=5
    a2=3
    b2=2
    c2=1
    a3=2
    b3=4
    c3=1
    x, y, z = meeting_planes(a1, b1, c1, a2, b2, c2, a3, b3, c3)
    print(f"Planes meet at x={x}, y={y} and z={z}")

if __name__ == "__main__":
    main()
