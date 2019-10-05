#!/usr/bin/python3

import numpy as np

def meeting_lines(a1, b1, a2, b2):
    # a1 *= -1
    # a2 *= -1
    A = np.array([[-b1, 1],[-b2, 1]])
    b = np.array([a1, a2])
    return np.linalg.solve(A, b)

def main():
    a1=1
    b1=4
    a2=3
    b2=2

    x, y  = meeting_lines(a1, b1, a2, b2)
    print(f"Lines meet at x={x} and y={y}")

if __name__ == "__main__":
    main()

"""
https://math.stackexchange.com/questions/1348380/intersection-of-two-planes-how-to-represent-a-line
y = a1*x + b1
y = a2*x + b2

1 = a1 + b1 
1 = a2 + b2 
"""