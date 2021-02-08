import numpy as np
import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D
import motion_tracker as mt
import csv
import pandas as pd

df=pd.read_csv('train.csv', sep=',',header=None)

data_set = df.values

labels = data_set[:,-2]

labels = np.unique(labels)
for label in labels:

    data_class_index = np.where(data_set[:,-2]==label)
    num_samples = len(data_class_index[0])
    fig = plt.figure()
    for ind,data_point in enumerate(data_set[data_class_index]):

        x = data_point[:30]
        y = data_point[30:60]
        z = data_point[60:90]
        traj_x , traj_y , traj_z = mt.track_3d_motion(x,y,z,interval=0.001)
        ax = fig.add_subplot(num_samples/2, 2,ind+1, projection='3d')
        print(ind%2+1)
        print(ind/2 +1)
        ax.plot3D(traj_x, traj_y, traj_z, 'gray')

        ax.scatter3D(traj_x, traj_y, traj_z, c=traj_z, cmap='Greens')
        ax.set_xlabel('x-axis')
        ax.set_ylabel('y-axis')
        ax.set_zlabel('z-axis')
    plt.show()




