import matplotlib.pyplot as plt
from invKin import *
import math
import numpy as np

def plot(X, Y, Z):
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
    plt.pause(0.3)



# forward_kin(q1,q2,q3,q4,q5,q6)
fig = plt.figure()
ax = fig.add_subplot(111,projection = '3d')
d90= (math.pi)
i=np.linspace(0,d90,15)
for a in i:
    X,Y,Z=rrr_forward_kin(a,0,0,0,0,0)
    plot(X, Y, Z)
for a in i:
    X,Y,Z=rrr_forward_kin(d90,a,0,0,0,0)
    plot(X, Y, Z)
for a in i:
    X,Y,Z=rrr_forward_kin(d90,d90,a,0,0,0)
    plot(X, Y, Z)
# for a in i:
#     X,Y,Z=forward_kin(d90,d90,d90,a,0,0)
#     plot(X, Y, Z)
# for a in i:
#     X,Y,Z=_forward_kin(d90,d90,d90,d90,a,0)
#     plot(X, Y, Z)
# for a in i:
#     X,Y,Z=_forward_kin(d90,d90,d90,d90,d90,a)
#     plot(X, Y, Z)
