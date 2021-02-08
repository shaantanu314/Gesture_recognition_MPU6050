import numpy as np
import csv
import pandas as pd
import DBA
import matplotlib.pyplot as plt

df=pd.read_csv('train.csv', sep=',',header=None)

data_set = df.values

labels = data_set[:,-2]

labels = np.unique(labels)
for label in labels:
    data_class_index = np.where(data_set[:,-2]==label)
    num_samples = len(data_class_index[0])
    data_class = data_set[data_class_index]
    
    X = data_class[:,0:30]
    Y = data_class[:,30:60]
    Z = data_class[:,60:90]
    
    template_X = DBA.dba(X,30)
    template_Y = DBA.dba(Y,30)
    template_Z = DBA.dba(Z,30)
    plt.figure()
    num_samples = len(data_class)
    for ind,data_point in enumerate(data_class):

        x = data_point[:30]
        y = data_point[30:60]
        z = data_point[60:90]
        plt.subplot(num_samples+1,1,ind+1)
        plt.plot(x)
        plt.plot(y)
        plt.plot(z)
    plt.suptitle(label)
    plt.subplot(num_samples+1,1,num_samples+1)
    plt.plot(template_X)
    plt.plot(template_Y)
    plt.plot(template_Z)
    plt.title('template')
    plt.show()