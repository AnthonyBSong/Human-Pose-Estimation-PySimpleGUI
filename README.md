**# Human-Pose-Estimation-PySimpleGUI**  

This is a project where I created a script for Human Pose Estimation and then embedded it into a GUI I made using PySimpleGUI. I recently finished this the scripts over the summer (summer of 2023) and I am excited to share it.
This project was done 100% in python and so it can be rather clanky, but in the future I may try to move it to a HTML, CSS, JavaScript framework like Electron.js. 

For the Human Pose Estimation, the code can be found in PoseEstimator.py. I used OpenCV and MediaPipe. MediaPipe Pose which is the package I used to locate and draw keypoints for the body uses BlazePose, a lightweight convolutional neural network architecture for human pose detection. BlazePose is a network that produces 33 body points for one person and was designed for quick real time interface on low powered mobile devices. However, as discussed later in the GUI section, my project was not able to encapsulate BlazePose's potential to its fullest. For more information on MediaPipe, MediaPipe Pose, and BlazePose look to the three links listed below.

[**Click Here**](https://github.com/google/mediapipe) for more information on MediaPipe.  
[**Click Here**](https://github.com/google/mediapipe/blob/master/docs/solutions/pose.md) for more information on MediaPipe Pose.  
[**Click Here**](https://ai.googleblog.com/2020/08/on-device-real-time-body-pose-tracking.html) for more information on BlazePose.  

For the GUI portion, I used PySimpleGUI, tkinter, and Pillow (Image and ImageTk). The GUI has buttons that allow the user to run pose estimation on different files (images, videos, and personal computer cameras). It also has a file manager, where the user is able to select and view mp4 files or PNG/JPEG files from File Explorer, Nemo, Dolphin, Finder, etc.

