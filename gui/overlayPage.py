import tkinter as tk
from tkinter import ttk
import cv2
from PIL import Image, ImageTk
import threading
import time

class OverlayPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.controller = controller

        # Initialize webcam
        self.cap = cv2.VideoCapture(0)

        # Container frame for horizontal layout
        self.container_frame = tk.Frame(self)
        self.container_frame.pack(fill=tk.BOTH)

        # Start Page Button
        self.start_page_button = tk.Button(self.container_frame, text="Start Page",
                           command=lambda: controller.show_frame("StartPage"))
        #self.start_page_button.pack(side=tk.LEFT)
        self.start_page_button.grid(row=0, column=0, padx=5, pady=5, sticky='ew')

        # Create the Start Timer Button, packed inside container_frame horizontally
        self.btn_timer = ttk.Button(self.container_frame, text="Start Timer", command=self.timer_btn_press)
        #self.btn_timer.pack(side=tk.LEFT)
        self.btn_timer.grid(row=0, column=1, padx=5, pady=5, sticky='ew')

        # Adjust timer_frame to be inside container_frame and packed horizontally
        print("self.winfo_width()*0.55", self.winfo_width()*0.55)
        print("self.winfo_width()", self.winfo_screenwidth())
        self.timer_frame = tk.Frame(self.container_frame, width=int(self.winfo_screenwidth()*0.55))
        #self.timer_frame.pack(side=tk.LEFT)
        self.timer_frame.grid(row=0, column=3, padx=5, pady=5, sticky='ew')

        # Timer label, adjusted for horizontal layout
        self.timer_label = tk.Label(self.timer_frame, text="Timer Text", bg="yellow", fg="black")
        self.timer_label.pack()

        self.running = False
        self.timer_on = False
        self.timer_paused = False
        self.timer_start_time = None

        self.update_frame()  # Start the update loop for the video frames
    
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
        else:
            default_img = ImageTk.PhotoImage(Image.open("./imgs/360_F_526665446_z51DM27QvvoMZ9Gkyx9gr5mkjSOmjswR.jpg"))
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
        self.btn_timer.config(text="Reset Timer")

        self.timer_paused = False
        # Create the Timer Pause Button
        self.btn_timer_pause = ttk.Button(self.container_frame, text="Pause Timer", command=self.pause_timer)
        self.btn_timer_pause.grid(row=0, column=2, padx=5, pady=5, sticky='ew')

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