import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

def read_data(file):
    data = [i.strip().split() for i in open(file).readlines()]
    for i in range(len(data)):
        data[i] = [float(j) for j in data[i]]
    data = np.array(data)

    return data

def plot_data(data):
    fig = plt.figure()
    ax = plt.axes(projection='3d')
    x = np.take(data,0,1)
    y = np.take(data,1,1)
    z = np.take(data,2,1)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    ax.set_xlim(-3,3)
    ax.set_ylim(0,2)
    ax.set_zlim(0,np.amax(z))
    ax.scatter3D(x, y, z, cmap='Greens');
    plt.show()

def plot_regression(data, NT, o0, o1,o2, v, i, learning_rate, rae):
    
    ax = plt.axes()
    ax.set_xlabel('y')
    ax.set_ylabel(v)
    if(o2==0):
        title = v+' = '+str(o0)+' + '+str(o1)+'y'+'\nEpochs: '+str(i)+'\nLearning rate: '+str(learning_rate)+'\nRAE: '+str(rae)
    else:
        title = v+' = '+str(o0)+' + '+str(o1)+'y'+' + '+str(o2)+'y^2'+'\nEpochs: '+str(i)+'\nLearning rate: '+str(learning_rate)+'\nRAE: '+str(rae)
    ax.set_title(title)

    NTy = np.take(NT,0,1)
    NTv = np.take(NT,1,1)

    y = np.take(data,1,1)

    if v == 'x':
        vv = np.take(data,0,1)

    if v == 'z':
        vv = np.take(data,2,1)

    plt.scatter(y, vv, cmap='Greens')
    plt.plot(NTy, NTv)

    plt.show()
