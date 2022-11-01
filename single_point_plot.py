import matplotlib.pyplot as plt
from invKin import *
import math
import numpy as np


def plot(X,Y,Z,fig,ax):
    ax.cla()
    X = np.reshape(X, (1, 7))
    Y = np.reshape(Y, (1, 7))
    Z = np.reshape(Z, (1, 7))
    ax.plot_wireframe(X, Y, Z)

    ax.set_xlim3d([-1, 1])
    ax.set_ylim3d([-1, 1])
    ax.set_zlim3d([-1, 1])
    ax.set_xlabel('x axis')
    ax.set_ylabel('y axis')
    ax.set_zlabel('z axis')
    ax.scatter(X, Y, Z)
    # ax.plot(X, Y, Z)
    plt.pause(100)

class linear_move:
    def __init__(self):
        self.InitPlot()
        self.InitArmPosition()
    def InitArmPosition(self):
        # initialized  q location
        self.px=1
        self.py = 1
        self.pz = 1
        roll=1
        pitch=1
        yaw=1
        q1,q2,q3,q4,q5,q6 = get_angles(self.px,self.py,self.pz,roll,pitch,yaw)
        print(f"{q1}, {q2}, {q3}, {q4}, {q5}, {q6}")
        X,Y,Z = forward_kin(q1,q2,q3,q4,q5,q6)
        plot(X, Y, Z, self.fig, self.ax)
    def InitPlot(self):
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111, projection='3d')

#
#
# roll = pitch = yaw = 1
# prab_num_points = 30
# M = create_parbolic_vector([px, py, self.pz], [self.px_new, self.py_new, self.pz_new], 1, prab_num_points)
#
# for i in range(prab_num_points):
#     q1, q2, q3, q4, q5, q6 = get_angles(M[i, 0], M[i, 1], M[i, 2], roll, pitch, yaw)
#     print(f"{q1}, {q2}, {q3}, {q4}, {q5}, {q6}")
#     X, Y, Z = forward_kin(q1, q2, q3, q4, q5, q6)
#     n_update_plot(X, Y, Z, self.fig, self.ax)




def main():
    linear_move()

if __name__ == "__main__":
        main()