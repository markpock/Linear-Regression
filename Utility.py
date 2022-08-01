import matplotlib.pyplot as plt

class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y
    
    def __str__(self):
        return '(' + str(self.x) + ', ' + str(self.y) + ')'

    def __repr__(self):
        return self.__str__()


def scatter_add(plist):
    x, y = [], []
    for p in plist:
        x.append(p.x)
        y.append(p.y)
    plt.scatter(x, y)