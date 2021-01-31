import serial
import matplotlib.pyplot as plt
import thread
import time
import numpy as np 
import pandas as pd
import sys

DEST_FILE = "./train.csv"


confx = 0
confy = 0
confz = 0

serialPort = serial.Serial(port = "/dev/ttyUSB0", baudrate=115200,bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE)
window = 50
index,acc_x,acc_y,acc_z = np.linspace(1,50,50),np.zeros((1,window)),np.zeros((1,window)),np.zeros((1,window))

def get_serial_data(live_data=True):
    if live_data == True:
        fig = plt.figure()
        ax = fig.add_subplot(111)
        fig.show()
    global index,acc_x,acc_y,acc_z,window
    global serialPort
    i=window+1
    thread.start_new_thread(train_mode,())
    while(1):
        data_string = None
        # Wait until there is data waiting in the serial buffer
        if(serialPort.in_waiting > 0):
            # print('*')
            index = np.append(index,i)
            # Read data out of the buffer until a carraige return / new line is found
            serialString = serialPort.readline()

            # Print the contents of the serial data
            data_string = serialString.decode('Ascii')
            data = data_string.split(',')

            acc_x = np.append(acc_x,float(data[0])/100)
            acc_y = np.append(acc_y,float(data[1])/100)
            acc_z = np.append(acc_z,float(data[2])/100)
            # print(acc_x.shape)
            if len(acc_x) > 400:
                acc_x = acc_x[-400:]
                acc_y = acc_y[-400:]
                acc_z = acc_z[-400:]
                index = index[-400:]
            if live_data == True:
                ax.clear()
                ax.plot(index[-window:],acc_x[-window:])
                ax.plot(index[-window:],acc_y[-window:])
                ax.plot(index[-window:],acc_z[-window:])
                fig.canvas.draw()
            i+=1

def dump_to_file(data_point,filepath):
    f = open(filepath,'a+')
    for feature in data_point:  
        f.write(str(feature)+',')
    f.write('\n')
    f.close()


def configure_pen():
    global acc_x,acc_y,acc_z
    time.sleep(5)
    confx = np.mean(acc_x)
    confy = np.mean(acc_y)
    confz = np.mean(acc_z)

    return confx,confy,confz

def train_mode():
    global acc_x,acc_y,acc_z
    global confx,confy,confz
    global DEST_FILE

    print("[Training Mode activated]")
    print("[Commands]\n1. 'start' - start training \n2. 'exit' - exit training mode\n3. 'conf' - configure the pen")
    while True:
        command = raw_input("Type command here: ")
        if command == "exit":
            print("[Exiting Training Mode]")
            return
        if command == "conf":
            print('Configuring...')
            confx,confy,confz = configure_pen()
        if command == "start":
            print("training starting in ...") 
            for i in xrange(3,0,-1):
                sys.stdout.write(str(i)+' ')
                sys.stdout.flush()
                time.sleep(1)

            print("[training ...]")
            time.sleep(2.5)
            curr_x = acc_x[-30:] -confx
            curr_y = acc_y[-30:] -confy
            curr_z = acc_z[-30:] -confz
            print("training data collected")
            data_point = np.array([])
            data_point = np.append(data_point,curr_x)
            data_point = np.append(data_point,curr_y)
            data_point = np.append(data_point,curr_z)
            label = raw_input("Enter the label for the input data or type 'DEL' to discard current data point : ")
            if label == "DEL":
                print("Discarded the data point")
                continue
            else:
                data_point = np.append(data_point,label)
                try:
                    dump_to_file(data_point,DEST_FILE)
                except Exception as e:
                    print(e)
                








def predict_mode():
    global acc_x,acc_y,acc_z

    while True:
        time.sleep(0.3)
        
        

if __name__ == "__main__":
    args = sys.argv
    n = len(args)
    if n>1:    
        if args[1] == "livedata":
            get_serial_data(live_data=True)
    else:
        get_serial_data(live_data=False)

    