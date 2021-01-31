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
    plt.figure()
    data_class_index = np.where(data_set[:,-2]==label)
    num_samples = len(data_class_index[0])
    print(data_class_index[0])
    for ind,data_point in enumerate(data_set[data_class_index]):

        x = data_point[:30]
        y = data_point[30:60]
        z = data_point[60:90]
        plt.subplot(num_samples,1,ind+1)
        plt.plot(x)
        plt.plot(y)
        plt.plot(z)
    plt.suptitle(label)
    plt.show()




# print(data_set.shape)
# for data_point in data_set:
#     ind = np.linspace(1,300,300)
#     x = data_point[:100]
#     y = data_point[100:200]
#     z = data_point[200:300]
#     label = data_point[-1]
#     x -= np.mean(x)
#     y -= np.mean(y)
#     z -= np.mean(z)
#     traj_x , traj_y , traj_z = mt.track_3d_motion(x,y,z,interval=0.01)
#     fig = plt.figure()
#     ax = plt.axes(projection='3d')
#     ax.plot3D(traj_x, traj_y, traj_z, 'gray')

#     ax.scatter3D(traj_x, traj_y, traj_z, c=traj_z, cmap='Greens')
#     ax.set_xlabel('x-axis')
#     ax.set_ylabel('y-axis')
#     ax.set_zlabel('z-axis')
#     plt.show()
    
