import matplotlib.pyplot as plt
import numpy as np
import itertools

#refference  https://math.stackexchange.com/questions/4177154/find-equation-for-a-parabolic-line-that-goes-through-two-points-in-3d-space
# y=1−x2 , or c⃗ (t)=(t,1−t2)

def create_parbolic_vector(start_p,end_p,high,samples):
    # A is start point, B end point, C mid point, D - maximum vertex to C

    A=np.array([start_p]).T
    B=np.array([end_p]).T
    d=high
    C = (A + B)/2
    D = C + np.array([[0,0,d]]).T
    t1 = np.linspace(-1,-0.5 , 10)
    t2 = np.linspace(-0.5, 0.5, 10)
    t3 = np.linspace(0.5, 1, 10)
    t= list(itertools.chain(t1,t2,t3))
    t=np.array(t)
    print(len(t))
    CC = np.tile(C, (1,len(t)))
    tt = np.tile(t,(len(t),1))
    qq = 1-t**2
    qqq = np.tile(qq,(len(t),1))

    DD = np.tile(D-C,(1,len(t)))
    EE = np.tile(C-A,(1,len(t)))

    X = CC + EE*t +DD*qq  #X=C+(C-A)t+(D-C)(1-t^2)
    X=X.T
    print(X)
    fig=plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.set_xlabel('x axis')
    ax.set_ylabel('y axis')
    ax.set_zlabel('z axis')
    ax.scatter(X[:,0],X[:,1],X[:,2])
    ax.scatter(A[0],A[1],A[2])
    ax.scatter(B[0], B[1], B[2])

    fig=plt.figure()
    plt.scatter(X[:,0],t)
    fig = plt.figure()
    plt.scatter(X[:, 1], t)
    fig = plt.figure()
    plt.scatter(X[:, 2], t)
    plt.show()
    return  X[:,0]

    plt.show()

#def main():
# create_parbolic_vector([-0.75,3.23,2.77],[1.57,0.94,0.74],100)
create_parbolic_vector([1,1,1],[2,2,2],4,50)