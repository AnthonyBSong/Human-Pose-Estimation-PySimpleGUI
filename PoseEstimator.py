import mediapipe as mp
import cv2

mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose
mp_holistic = mp.solutions.holistic

folder_path = 'C:/Users/antho/CS_projects/PoseApp/'

class PoseEstimator():
    def drawImageToBytes(cap):
        '''This method returns image with annotations'''
        with mp_pose.Pose(
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5) as pose:

            #read capture
            ret, frame = cap.read()

            if ret:
                # Convert the BGR image to RGB.
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                # To improve performance, optionally mark the frame as not writeable to
                # pass by reference.
                frame.flags.writeable = False
                results = pose.process(frame)

                # Draw the pose annotation on the frame.
                frame.flags.writeable = True
                frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
                mp_drawing.draw_landmarks(
                    frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)
                
                #resize and convert to png
                scale_percent = 85 # percent of original size
                width = int(frame.shape[1] * scale_percent / 100)
                height = int(frame.shape[0] * scale_percent / 100)
                dim = (width, height)
                frame = cv2.resize(frame, dim, fx=1, fy=1)
                ret, frame_png = cv2.imencode('.ppm', frame) #you can switch .ppm to .png if need be
                frame_byte = frame_png.tobytes()

        return ret, frame_byte

    def drawImageToBytes2(cap):
        '''This method returns image without annotations'''
        ret, frame = cap.read()

        if ret:
            # Convert the BGR image to RGB.
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            # To improve performance, optionally mark the frame as not writeable to
            # pass by reference.
            frame.flags.writeable = False

            # Draw the pose annotation on the frame.
            frame.flags.writeable = True
            frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
            
            #resize and convert to png
            scale_percent = 85 # percent of original size
            width = int(frame.shape[1] * scale_percent / 100)
            height = int(frame.shape[0] * scale_percent / 100)
            dim = (width, height)
            frame = cv2.resize(frame, dim, fx=1, fy=1)
            ret, frame_png = cv2.imencode('.ppm', frame) #you can switch .ppm to .png if need be
            frame_byte = frame_png.tobytes()

        return ret, frame_byte

    def runVideo(window, file = None, draw = True):
        '''Officially updates window images with annotated or unannotated images generated from video capture'''
        cap = cv2.VideoCapture(file)

        if file is None or not(file.lower().endswith(".mp4")):
            cap = cv2.VideoCapture(0)

        #replace value of file as None since we have already uploaded to runVideo
        file = None

        while cap.isOpened():   
            event, values = window.read(timeout=10)

            if draw:
                ret, frame_byte = PoseEstimator.drawImageToBytes(cap)
            else:
                ret, frame_byte = PoseEstimator.drawImageToBytes2(cap)

            if event in {"_camera_", "_video_", "_image_"}:
                window['-IMAGE-'].update(folder_path + "PoseAppDS.png")
                window['-TOUT-'].update("")
                break

            window['-IMAGE-'].update(data=frame_byte)

        cap.release()

    def drawStaticImage(window, file):
        '''Officially update window image with annotated image generated from image file'''
        event, values = window.read(timeout=10)

        if file is None or not(file.lower().endswith((".png", ".jpg"))):
            return


        if event == "_image_":
            window['-IMAGE-'].update("C:/Users/antho/CS_projects/PoseApp/PoseAppDS.png")
            window['-TOUT-'].update("")
            return  
        
        image = cv2.imread(file)

        with mp_pose.Pose(
        static_image_mode=True,
        model_complexity=2,
        min_detection_confidence=0.5) as pose:
            image_height, image_width, _  = image.shape
            # Convert the BGR image to RGB before processing.
            results = pose.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
            annotated_image = image.copy() 
            # Draw pose landmarks on the copy of the image.
            mp_drawing.draw_landmarks(annotated_image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)
            #resize image
            scale_percent = 85 # percent of original size
            width = int(annotated_image.shape[1] * scale_percent / 100)
            height = int(annotated_image.shape[0] * scale_percent / 100)
            dim = (width, height)
            dim = (width, height)
            annotated_image = cv2.resize(annotated_image, dim, fx=1, fy=1)
            #convert annotated_image to bytes
            _, picture = cv2.imencode('.ppm', annotated_image)
            picture_bytes = picture.tobytes()
            window["-IMAGE-"].update(data=picture_bytes)