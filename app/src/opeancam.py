import pickle 
from PIL import Image, ImageDraw
import cv2
import customtkinter as ctk
# from ..ui.home import LiveCamera
from app.globals import GLOBAL
from .facerec import rec_face
import os

# check the encodings in the location
encoding_loc = os.path.join(os.getcwd(),"app", "data", "saved", "encodings.pickle")

class Cam(ctk.CTkFrame):
    def __init__(self,master,**kwargs):
        super().__init__(master,**kwargs)
        self.cap=None
        # self.livecam=LiveCamera(self)
        
        with open(encoding_loc, mode="rb") as f:
            self.encodings = pickle.load(f)
            self.known_face_encodings = self.encodings[0]
            self.known_face_names = self.encodings[1]


    def toggle_camera(self):
        self.livecam=GLOBAL['livecam']

        if self.cap is None:
            # Start camera capture
            self.cap = cv2.VideoCapture(0) 
            self.update_frame() 
            self.livecam.title.configure(text="")
            # self.livecam.title.configure(command=self.cap)
        else:
            # Stop camera capture
            # self.livecam.title.configure(text="LIVE CAMERA")
            self.cap.release()
            self.cap = None
            # self.start_button.config(text="START CAMERA")

    def update_frame(self):
        self.livecam=GLOBAL['livecam']

        if self.cap is not None:
            # Capture frame-by-frame
            ret, frame = self.cap.read()
            _img = Image.fromarray(frame)
            draw = ImageDraw.Draw(_img)
            # Convert BGR to RGB for tkinter compatibility
            # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
            face_location,face_names=rec_face(frame,self.known_face_encodings, self.known_face_names)

            print(face_location,face_names)
            for face, name in zip(face_location, face_names):
                _display_face(draw, face, name)
            img = ctk.CTkImage(_img, size=(600,400))

            # Update the label with the camera frame
            self.livecam.title.configure(image=img)

            # Schedule the next frame update using tkinter's after() method
            self.master.after(10, self.update_frame)


def _display_face(draw, bounding_box, name, clr="white"):
    top, right, bottom, left = bounding_box
    draw.rectangle(((left, top), (right, bottom)), outline=clr)
    text_left, text_top, text_right, text_bottom = draw.textbbox(
        (left, bottom), name
    )
    draw.rectangle(
        ((text_left, text_top), (text_right, text_bottom)),
        fill=clr,
        outline=clr,
    )
    draw.text(
        (text_left, text_top),
        name,
        fill="white",
    )
