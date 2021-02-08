# Hand Gesture Recognition  using MPU6050 ( English Alphabet Detection)

This is a project based on hand Gesture Detection using the accelerometer and gyroscope values from mpu6050 . The real time sensor data is also plotted in a window while running the program.

# Dynamic Time Wrapping 
In time series analysis, **Dynamic time warping (DTW**) is one of the algorithms for measuring similarity between two temporal sequences, which may vary in speed. For instance, similarities in walking could be detected using DTW, even if one person was walking faster than the other, or if there were accelerations and decelerations during the course of an observation. DTW has been applied to temporal sequences of video, audio, and graphics data  indeed, any data that can be turned into a linear sequence can be analyzed with DTW.
In this project, we want to compare the time series ,ie, the 3-axis accelerometer data and find similarities between them so that we can build a model which can predict the gesture ,ie, letters of english alphabets.


# DTW Barycenter Averaging algorithm
### Template generation for DTW

We have used , **DTW Barycenter Averaging algorithm** to generate template of each class and during 'predict mode' , we can run DTW to calculate distance between these templates and the testing time series to predict the gesture.


## Implementation Specific

### The program has two modes
- Train Mode
- Predict Mode

 ### Train mode can be used to add new gestures to the dataset while predict mode is used to predict the gestures (real-time testing)

- train.csv has the dataset generated using MPU6050 sensor
- reader.py is the main program which acts as interface with MPU6050 is 

### Visualization
- Run analysis.py   to visualize the plots of the dataset of each class
- Run trajectory.py to visualize the 3-D motion of the pen on a 3D plot

### DTW algorithm
- The DTW Barycenter Average algorithm and DTW algorithms are implemented in DBA.py
