import PySimpleGUI as sg
import numpy as np
import time
import os.path
from PIL import Image, ImageTk
import tkinter as tk
from PoseEstimator import PoseEstimator

class Application():
    def __init__(self, GUIcolor = 'DarkAmber', folder_path = 'C:/Users/antho/CS_projects/PoseApp/'):
        self.file = None
        self.folder_path = folder_path

        sg.theme(GUIcolor)
        self.file_column = [
            [
                sg.Text("Image Folder"),
                sg.In(size=(25, 1), enable_events=True, key="-FOLDER-"),
                sg.FolderBrowse(),
            ],
            [
                sg.Listbox(
                    values=[], enable_events=True, size=(45, 24), key="-FILE LIST-"
                )
            ],
            [sg.Button('image', key='_image_'),
            sg.Button('video', key='_video_'),
            sg.Button('camera', key='_camera_')]
        ]

        sg.theme(GUIcolor)
        self.image_column = [[sg.Text(size=(50, 1), key="-TOUT-")],
                        [sg.Image(filename=self.folder_path + 'PoseAppDS.png', key='-IMAGE-')]]
        
        sg.theme('DarkAmber')
        # ----- Full layout -----
        self.video_layout = [
            [
                sg.Column(self.file_column),
                sg.VSeperator(),
                sg.Column(self.image_column),
            ]
        ]

    def run(self):
        window = sg.Window(title='Video Player', layout=self.video_layout, size=(1000, 500), margins=(10, 10), enable_close_attempted_event=True) 

        while True:
            event, values = window.read(timeout=10)

            if event == sg.WINDOW_CLOSE_ATTEMPTED_EVENT and sg.popup_yes_no('Do you really want to exit?') == 'Yes':
                break

            if event == "-FOLDER-":
                folder = values["-FOLDER-"]
                try:
                    # Get list of files in folder
                    file_list = os.listdir(folder)
                except:
                    file_list = []

                fnames = [
                    f
                    for f in file_list
                    if os.path.isfile(os.path.join(folder, f))
                    and f.lower().endswith((".png", ".jpg", ".gif", ".mp4"))
                ]
                window["-FILE LIST-"].update(fnames)

            if event == "-FILE LIST-":  # A file was chosen from the listbox
                try:
                    filename = os.path.join(
                        values["-FOLDER-"], values["-FILE LIST-"][0]
                    ).replace("\\", "/")

                    #convert filename to a png if jpg.
                    if filename.lower().endswith((".jpg", ".png")):
                        image = Image.open(filename)
                        image.thumbnail((600, 600))
                        photo_img = ImageTk.PhotoImage(image)
                        self.file = filename
                        window["-TOUT-"].update(filename)
                        window["-IMAGE-"].update(data=photo_img)

                    elif filename.lower().endswith((".mp4")):
                        self.file = filename
                        window["-TOUT-"].update("Please remember to close camera/video!")
                        PoseEstimator.runVideo(window, self.file, False)

                except:
                    pass

            if event == "_camera_":
                window["-TOUT-"].update("Please remember to close camera/video!")
                PoseEstimator.runVideo(window)

            if event == "_video_":
                window["-TOUT-"].update("Please remember to close camera/video!")
                PoseEstimator.runVideo(window, self.file)
            
            if event == "_image_":
                PoseEstimator.drawStaticImage(window, self.file)
        
        window.close()

if __name__ == "__main__":
    a = Application()
    a.run()