import matplotlib.pyplot as plt
import numpy as np
from Utility import scatter_add, Point
from Execution import exec_regression


def line(x, xcent, slope, intercept):
    return slope * (x - xcent) + intercept


def line_add(plist, slope, intercept, xcent):
    maxpt, minpt = plist[0], plist[0]
    for p in plist:
        if p.x > maxpt.x:
            maxpt = p
        if p.x < minpt.x:
            minpt = p
    spatz = np.linspace(minpt.x, maxpt.x, 100)
    plt.plot(spatz, line(spatz, xcent, slope, intercept))


def main():
    x = np.random.normal(150, 10, size=15)
    y = np.pi * x + np.random.normal(0, 4, size=15)

    points = [Point(xi, yi) for xi, yi in zip(x, y)]
    scatter_add(points)
    slope, intercept, xcent = exec_regression(points)
    line_add(points, slope, intercept, xcent)
    print('Slope:', slope, '\nIntercept:', line(0, xcent, slope, intercept))
    plt.show()


if __name__ == '__main__':
    main()