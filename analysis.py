import numpy as np
import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D
import motion_tracker as mt
import csv

data_set = np.genfromtxt('train.csv',delimiter=',')

for data_point in data_set:
    ind = np.linspace(1,200,200)
    x = data_point[:200]
    y = data_point[200:400]
    z = data_point[400:600]
    label = data_point[-1]
    x -= np.mean(x)
    y -= np.mean(y)
    z -= np.mean(z)
    traj_x , traj_y , traj_z = mt.track_3d_motion(x,y,z,interval=0.01)
    fig = plt.figure()
    ax = plt.axes(projection='3d')
    ax.plot3D(traj_x, traj_y, traj_z, 'gray')

    ax.scatter3D(traj_x, traj_y, traj_z, c=traj_z, cmap='Greens')
    ax.set_xlabel('x-axis')
    ax.set_ylabel('y-axis')
    ax.set_zlabel('z-axis')
    plt.show()
    