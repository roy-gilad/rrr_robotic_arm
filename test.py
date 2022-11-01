import matplotlib.pyplot as plt
import numpy
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import time

def make_plot(ax,fig,X,Y,Z):
    ax.cla()
    ax.set_xlim3d([0, 5])
    ax.set_ylim3d([0, 5])
    ax.set_zlim3d([0, 5])
    ax.scatter(X,Y,Z)
    ax.plot(X,Y,Z)
    plt.pause(0.5)

def main():
    xpoints = np.array([1, 8])
    ypoints = np.array([3, 10])

    plt.plot(xpoints, ypoints)
    plt.show()

    # x=0
    # X=[1,2,3]
    # Y=[1,5,3]
    # Z=[1,1,4]
    # fig = plt.figure()
    # ax = fig.add_subplot(111, projection='3d')
    # make_plot(ax,fig,X, Y, Z)
    # for i in range(7):
    #     x+=0.1
    #     X = [x, 2, 3]
    #     Y = [1, 5, 3]
    #     Z = [1, 1, 4]
    #     make_plot(ax, fig, X, Y, Z)
    # plt.show()



