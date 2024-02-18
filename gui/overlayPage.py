import tkinter as tk
from tkinter import ttk
import cv2
from PIL import Image, ImageTk
import threading
# import customtkinter as ctk
import time
import hand_gestures
import threading

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
        self.container_frame.grid_columnconfigure(0, weight=1)  # Empty side column for centering
        self.container_frame.grid_columnconfigure(1, weight=0)  # Column for the "Start Page" button
        self.container_frame.grid_columnconfigure(2, weight=0)  # Column for the "Start Timer" button
        self.container_frame.grid_columnconfigure(3, weight=0)  # Column for the "Pause Timer" button (dynamically added)
        self.container_frame.grid_columnconfigure(4, weight=0)  # Column for additional elements if needed
        self.container_frame.grid_columnconfigure(5, weight=0)  # Empty side column for centering
        self.container_frame.grid_columnconfigure(6, weight=0)  # Empty side column for centering
        self.container_frame.grid_columnconfigure(7, weight=0)  # Empty side column for centering
        self.container_frame.grid_columnconfigure(8, weight=1)  # Empty side column for centering


        # Start Page Button
        self.start_page_button = ttk.Button(self.container_frame, text="Back to Home",
                           command=lambda: controller.show_frame("StartPage"))

        self.start_page_button.grid(row=0, column=1, padx=5, pady=5, sticky='ew')

        # Create the Start Timer Button
        self.btn_timer = ttk.Button(self.container_frame, text="Start Timer", command=self.timer_btn_press)
        self.btn_timer.grid(row=0, column=2, padx=5, pady=5, sticky='ew')

        # Frame to contain timer
        self.timer_frame = ttk.Frame(self.container_frame)
        self.timer_frame.grid(row=0, column=4, padx=5, pady=5, sticky='ew')

        # Timer label
        self.timer_label = tk.Label(self.timer_frame, text="Timer Text", bg="yellow", fg="black", width=20)
        self.timer_label.pack()

        # Button to launch focus with overlay
        self.btn_launch_focus_with_overlay = ttk.Button(self.container_frame, text="Launch Focus With Overlay", command=self.launch_focus_with_overlay)
        self.btn_launch_focus_with_overlay.grid(row=0, column=5, padx=5, pady=5, sticky='ew')

        # Frame to contain symbol label
        self.symbol_frame = ttk.Frame(self.container_frame)
        self.symbol_frame.grid(row=0, column=7, padx=5, pady=5, sticky='ew')

        # Create label to hold symbol for gesture
        self.gesture_label = ttk.Button(self.symbol_frame, text="Gesture",  width=30, command = self.gesture_btn_press)
        self.gesture_label.pack()

        #self.gesture_label = ttk.Button(self.symbol_frame, text="Stop Gesture", width=30,
        #                                command= self.stop_gesture_btn_press)
        #self.gesture_label.pack()

        self.running = False
        self.timer_on = False
        self.timer_paused = False
        self.timer_start_time = None
        self.focus_with_overlay_launched = False

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
        self.btn_timer_pause.grid(row=0, column=3, padx=5, pady=5, sticky='ew')

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

    def launch_focus_with_overlay(self):
        if self.focus_with_overlay_launched:
            self.message_frame.destroy()
            self.message_label.destroy()
            self.focus_with_overlay_launched = False
            self.btn_launch_focus_with_overlay.config(text="Launch Focus With Overlay")
        else:
            # Create frame to contain message
            self.message_frame = tk.Frame(self.container_frame)
            self.message_frame.grid(row=0, column=6, padx=5, pady=5, sticky='ew')

            # Create message label
            self.message_label = tk.Label(self.message_frame, text="Focus Text", bg="red", fg="black", width=30)
            self.message_label.pack()

            self.focus_with_overlay_launched = True
            self.btn_launch_focus_with_overlay.config(text="End Focus With Overlay")

    def gesture_btn_press(self):
        if hand_gestures.keep_running == False:
            hand_gestures.keep_running = True
            self.gesture_thread = threading.Thread(target = hand_gestures.main)
            self.gesture_thread.start()
        else:
            hand_gestures.keep_running = False
            if hasattr(self, 'gesture_thread') and self.gesture_thread.is_alive():
                self.gesture_thread.join()

    def stop_gesture_btn_press(self):
        hand_gestures.keep_running = False
        if hasattr(self, 'gesture_thread') and self.gesture_thread.is_alive():
            self.gesture_thread.join()
