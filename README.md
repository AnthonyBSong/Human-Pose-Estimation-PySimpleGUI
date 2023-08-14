**# Human-Pose-Estimation-PySimpleGUI**
This is a project where I created a script for Human Pose Estimation and then embedded it into a GUI I made using PySimpleGUI. I recently finished this the scripts over the summer (summer of 2023) and I am excited to share it.
This project was done 100% in python and so it can be rather clanky, but in the future I may try to move it to a HTML, CSS, JavaScript framework like Electron.js. 

For the Human Pose Estimation, the code can be found in PoseEstimator.py. I used OpenCV and MediaPipe. MediaPipe Pose uses BlazePose, which is a lightweight convolutional neural network architecture for human pose detection. It
was designed for quick real time interface on low powered mobile devices. However, as discussed later in the GUI section, my project was not able to encapsulate BlazePose's potential to its fullest. For further information on 
MediaPipe, MediaPipe Pose, and BlazePose look to below links.

[**Click Here**](https://github.com/google/mediapipe) for more information on MediaPipe.
[**Click Here**](https://github.com/google/mediapipe/blob/master/docs/solutions/pose.md) for more information on MediaPipe Pose.
[**Click Here**](https://ai.googleblog.com/2020/08/on-device-real-time-body-pose-tracking.html) for more information on BlazePose.
