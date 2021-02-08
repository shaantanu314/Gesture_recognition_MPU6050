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


