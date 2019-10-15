#!/usr/bin/env python3
import math
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

def fit_line(x, y):
    fm = LinearRegression(fit_intercept = True)
    fm.fit(x[:, None], y)
    intercept = fm.intercept_
    slope = fm.coef_
    return slope[0], intercept

def main():
    x1 = np.linspace(1, 100, 100)
    # x2 = np.array([0,1,2,3,4,5,6,7,8,9])
    y1 = 4 * x1 * np.random.randn(100) + 12 + 1 * np.random.randn(100)
    # y2 = math.sqrt(2) + x2 * np.random.randn(10) 
    slope1, intercept1 = fit_line(x1,y1)
    # slope2, intercept2 = fit_line(x2,y2)
    print("Slope:", slope1)
    print("Intercept:", intercept1)
    # print("Slope:", slope2)
    # print("Intercept:", intercept2)
    plt.plot(x1, x1 * slope1 + intercept1)
    plt.plot(x1, y1, "o")
    # plt.plot(np.vstack([x1,x1]), np.vstack([x1 * slope1 + intercept1, y1]))
    
    # plt.plot(x2, x2 * slope2 + intercept2)
    # plt.plot(x2, y2, "o")
    # plt.plot(np.vstack([x2,x2]), np.vstack([x2 * slope2 + intercept2, y2]))
    plt.show()

if __name__ == "__main__":
    main()
