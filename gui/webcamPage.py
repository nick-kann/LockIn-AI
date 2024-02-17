import tkinter as tk
from tkinter import ttk
import cv2
from PIL import Image, ImageTk
import threading
import time

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

        # Create the Start Timer Button
        self.btn_timer = ttk.Button(self.button_frame, text="Start Timer", command=self.timer_btn_press)
        self.btn_timer.pack(side=tk.LEFT, padx=5, pady=5)
        
        # Create the Stop Webcam button
        self.btn_stop = ttk.Button(self.button_frame, text="Exit", command=exit)
        self.btn_stop.pack(side=tk.LEFT, padx=5, pady=5)

        self.video_frame = tk.Frame(self, width=640, height=480)
        
        # Adjustments to video label to place it inside video_frame
        self.video_label = tk.Label(self.video_frame)
        self.video_label.pack()

        self.video_frame.pack(padx=10, pady=10, expand=True)

        # Timer label
        self.timer_label = tk.Label(self.video_frame, text="Timer Text", bg="yellow", fg="black")
        self.timer_label.place(relx=0.7, rely=0, relwidth=0.3, relheight=0.2)
        self.timer_label.config(bg="yellow")
        self.timer_label.config(fg="black")
        self.timer_label.config(font=("Arial", 12))
        
        self.running = False
        self.timer_on = False
        self.timer_paused = False
        self.timer_start_time = None

        self.update_frame()  # Start the update loop for the video frames
    
    def start_webcam(self):
        if not self.running:
            self.running = True
    
    def stop_webcam(self):
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
        if self.timer_on and (not self.timer_paused):
            self.update_timer()

    def timer_btn_press(self):
        # If the timer rn is running
        if self.timer_on:
            self.stop_timer()
        else:
            self.start_timer()

    def update_timer(self):
        if not self.timer_start_time:
            return
        elapsed_time = time.time() - self.timer_start_time
        hours, remainder = divmod(elapsed_time, 3600)
        minutes, seconds = divmod(remainder, 60)
        milliseconds = (seconds - int(seconds)) * 1000
        self.timer_label.config(text=f"{int(hours):02}:{int(minutes):02}:{int(seconds):02}.{int(milliseconds):03}")

    def start_timer(self):
        self.timer_on = True
        self.timer_start_time = time.time()
        self.btn_timer.config(text="Stop Timer")

        # Create the Timer Pause Button
        self.btn_timer_pause = ttk.Button(self.button_frame, text="Pause Timer", command=self.pause_timer)
        self.btn_timer_pause.pack(side=tk.LEFT, padx=5, pady=5)
        self.timer_paused = False

    def stop_timer(self):
        self.timer_on = False
        self.btn_timer.config(text="Start Timer")
        self.btn_timer_pause.destroy()

        self.timer_label.config(text="Timer Text")

    def pause_timer(self):
        print("asfd")
        self.timer_paused = True
        self.btn_timer_pause.config(text="Unpause Timer", command=self.unpause_timer)

    def unpause_timer(self):
        self.timer_paused = False
        self.btn_timer_pause.config(text="Pause Timer", command=self.pause_timer)


        
    def __del__(self):
        if self.cap.isOpened():
            self.cap.release()
