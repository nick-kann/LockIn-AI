import tkinter as tk
from tkinter import ttk
import cv2
from PIL import Image, ImageTk
import threading
import time
from timert import TimerT

class WebcamPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.controller = controller

       # Initialize webcam
        self.cap = cv2.VideoCapture(0)

        # Create a frame for the buttons
        self.button_frame = ttk.Frame(self)
        self.button_frame.pack(fill=tk.X, side=tk.BOTTOM, expand=True)
        
        # Buttons
        self.btn_start = ttk.Button(self.button_frame, text="Start Webcam", command=self.start_webcam)
        self.btn_start.pack(side=tk.LEFT, padx=5, pady=5)
        
        self.btn_stop = ttk.Button(self.button_frame, text="Stop Webcam", command=self.stop_webcam)
        self.btn_stop.pack(side=tk.LEFT, padx=5, pady=5)

        # Create the Stop Webcam button
        self.btn_stop = ttk.Button(self.button_frame, text="Exit", command=exit)
        self.btn_stop.pack(side=tk.LEFT, padx=5, pady=5)

        self.video_frame = tk.Frame(self, width=940, height=480)
        self.video_frame.pack(padx=10, pady=10, expand=True)

        # Adjustments to video label to place it inside video_frame
        self.video_label = tk.Label(self.video_frame, bd=15)
        self.video_label.pack()

        # Create the Start Timer Button
        self.btn_timer = ttk.Button(self.button_frame, text="Start Timer")
        self.btn_timer.pack(side=tk.LEFT, padx=5, pady=5)
        self.btn_set_timer = ttk.Button(self.button_frame, text="Set Timer")
        self.btn_set_timer.pack(side=tk.LEFT, padx=5, pady=5)

        self.timer = TimerT(self.button_frame, self.btn_timer, self.btn_set_timer)
        self.btn_timer.config(command=self.timer.timer_btn_press)
        self.btn_set_timer.config(command=self.timer.set_timer)

        self.timer_label = tk.Label(self.video_frame, text="Timer Text", bg="#B7EDE8", fg="black", relief="solid", bd=4)
        self.timer_label.place(relx=0.8, rely=0, relwidth=0.2, relheight=0.1)
        self.timer_label.config(bg="#B7EDE8")
        self.timer_label.config(fg="black")
        self.timer_label.config(font=("Lato", 10, "bold"))
        self.timer.set_label(self.timer_label)
        
        self.running = False
        self.update_frame()  # Start the update loop for the video frames
    
    def start_webcam(self):
        if not self.running:
            self.timer.get_label().config(bd=10)
            self.timer.get_label().config(font=("Lato", 30, "bold"))
            self.running = True
    
    def stop_webcam(self):
        self.timer.get_label().timer_label.config(bd=4)
        self.timer.get_label().config(font=("Lato", 10, "bold"))
        self.running = False
        # Clear the video label
        self.video_label.config(image='')  # Clears the label
        # Optionally, you can set a placeholder text or a default image here
        self.video_label.config(text='Webcam stopped')  # Placeholder text
        # If setting a default image, you would do something like this:
        default_img = ImageTk.PhotoImage(Image.open("./imgs/360_F_526665446_z51DM27QvvoMZ9Gkyx9gr5mkjSOmjswR.jpg"))
        self.video_label.imgtk = default_img
        self.video_label.config(image=default_img)
    
    def update_frame(self):
        if self.running:
            # Capture the latest frame from the webcam
            ret, frame = self.cap.read()
            if ret:
                # Convert the image from BGR (OpenCV format) to RGB
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                # Convert the image to PIL format
                img = Image.fromarray(frame)
                # Convert the image for Tkinter
                imgtk = ImageTk.PhotoImage(image=img)
                # Update the label with the new image
                self.video_label.imgtk = imgtk
                self.video_label.configure(image=imgtk)
        else:
            default_img = ImageTk.PhotoImage(Image.open("./imgs/360_F_526665446_z51DM27QvvoMZ9Gkyx9gr5mkjSOmjswR.jpg"))
            self.video_label.imgtk = default_img
            self.video_label.config(image=default_img)
        self.parent.after(10, self.update_frame)  # Repeat after an interval
        if self.timer.timer_on and (not self.timer.timer_paused):
        if self.timer.timer_on and (not self.timer.timer_paused):   
            self.timer.update_timer()

    def __del__(self):
        if self.cap.isOpened():
            self.cap.release()
