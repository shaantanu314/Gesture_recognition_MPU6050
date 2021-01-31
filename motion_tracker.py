import numpy as np
import matplotlib.pyplot as plt

trajectory_x ,trajectory_y , trajectory_z = [],[],[]
pos = [0,0,0]
vel = [0,0,0]
dt = 0.01

def update_velocity(acc):

    vel[0] = vel[0] + acc[0]*dt
    vel[1] = vel[1] + acc[1]*dt
    vel[2] = vel[2] + acc[2]*dt

def update_position(acc):

    dx = vel[0]*dt + 0.5*acc[0]*dt**2
    dy = vel[1]*dt + 0.5*acc[1]*dt**2
    dz = vel[2]*dt + 0.5*acc[2]*dt**2
    pos[0] = pos[0] + dx
    pos[1] = pos[1] + dy
    pos[2] = pos[2] + dz

def append_position():

    trajectory_x.append(pos[0])
    trajectory_y.append(pos[1])
    trajectory_z.append(pos[2])

def clear_path():
    del trajectory_x[:]
    del trajectory_y[:]
    del trajectory_z[:]

def track_3d_motion(x,y,z,interval=0.1):

    dt = interval
    clear_path()
    pos = [0,0,0]
    vel = [0,0,0]
    for i in range(x.shape[0]):
        acc = [x[i],y[i],z[i]]
        append_position()
        update_position(acc)
        update_velocity(acc)
        
   
       
    return (trajectory_x , trajectory_y , trajectory_z)