**# Human-Pose-Estimation-PySimpleGUI**  

This is a project where I created a script for Human Pose Estimation and then embedded it into a GUI I made using PySimpleGUI. I recently finished this the scripts over the summer (summer of 2023) and I am excited to share it.
This project was done 100% in python and so it can be rather clanky, but in the future I may try to move it to a HTML, CSS, JavaScript framework like Electron.js. Below is a video demonstrating what my script does.

Add video here!

For the Human Pose Estimation, the code can be found in PoseEstimator.py. I used OpenCV and MediaPipe. MediaPipe Pose which is the package I used to locate and draw keypoints for the body uses BlazePose, a lightweight convolutional neural network architecture for human pose detection. BlazePose is a network that produces 33 body points for one person and was designed for quick real time interface on low powered mobile devices. However, as discussed later in the GUI section, my project was not able to encapsulate BlazePose's potential to its fullest. For more information on MediaPipe, MediaPipe Pose, and BlazePose look to the three links listed below.

[**Click Here**](https://github.com/google/mediapipe) for more information on MediaPipe.  
[**Click Here**](https://github.com/google/mediapipe/blob/master/docs/solutions/pose.md) for more information on MediaPipe Pose.  
[**Click Here**](https://ai.googleblog.com/2020/08/on-device-real-time-body-pose-tracking.html) for more information on BlazePose.  

**A quick peek at human pose estimation on images using MediaPipe Pose**
![Screenshot 2023-08-14 230603](https://github.com/AnthonyBSong/Human-Pose-Estimation-PySimpleGUI/assets/62223817/f72d0b75-1046-43ea-907d-8059aeaaa02a)


For the GUI portion, I used PySimpleGUI, tkinter, and Pillow (Image and ImageTk). The Human Pose Estimation script I wrote returned .ppm images, and I converted these .ppm images into byte data to be updated and displayed to the PySimpleGUI image element. Because the script returned image by image and there was some conversion involved, the GUI could not display camera capture and video files at the 30 FPS that it is capable of doing when using cv2.imshow(). I am trying to find a way to embed a cv2.imshow() into a PySimpleGUI element, although I have not found any support for that currently. Future plans may be to switch from PySimpleGUI image elements to PySimpleGUI slide elements as those may be better suited for displayed image after image in a fashion similar to a video.



As for the rest of the GUI, there are PySimpleGUI buttons titled image, video, and camera that allow the user to run pose estimation on different inputs. There is a file manager, where the user is able to select and view mp4 files or PNG/JPEG files from their computer's File Explorer, Finder, Nemo, Dolphin, etc before they click the buttons to run pose estimation. Finally, there are text outputs to show the path of the file clicked in the file manager as well as directions for how to use the app.

**A quick peek at the graphic user interface**
![Screenshot 2023-08-14 225550](https://github.com/AnthonyBSong/Human-Pose-Estimation-PySimpleGUI/assets/62223817/b16e3a93-814a-49a1-9407-5fb4b51bcafb)

Please change self.folder_path parameters in 
