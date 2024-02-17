import tkinter as tk
from tkinter import ttk
import cv2
from PIL import Image, ImageTk
import threading

class WebcamApp:
    def __init__(self, window, window_title):
        self.window = window
        self.window.title(window_title)
        
        # Initialize the webcam
        self.cap = cv2.VideoCapture(0)
        
        # Create a frame for the buttons
        self.button_frame = ttk.Frame(self.window)
        self.button_frame.pack(fill=tk.X, side=tk.BOTTOM)
        
        # Create the Start Webcam button
        self.btn_start = ttk.Button(self.button_frame, text="Start Webcam", command=self.start_webcam)
        self.btn_start.pack(side=tk.LEFT, padx=5, pady=5)
        
        # Create the Stop Webcam button
        self.btn_stop = ttk.Button(self.button_frame, text="Stop Webcam", command=self.stop_webcam)
        self.btn_stop.pack(side=tk.LEFT, padx=5, pady=5)

        # Create the Stop Webcam button
        self.btn_stop = ttk.Button(self.button_frame, text="Button 3", command=self.stop_webcam)
        self.btn_stop.pack(side=tk.LEFT, padx=5, pady=5)
        
        # Create the Stop Webcam button
        self.btn_stop = ttk.Button(self.button_frame, text="Button 4", command=self.stop_webcam)
        self.btn_stop.pack(side=tk.LEFT, padx=5, pady=5)

        # Create a label to display the video frames
        self.video_label = tk.Label(self.window)
        self.video_label.pack(padx=10, pady=10, expand=False)
        
        self.running = False
        self.update_frame()  # Start the update loop for the video frames
        
        self.window.mainloop()
    
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
        self.window.after(10, self.update_frame)  # Repeat after an interval
        
    def __del__(self):
        if self.cap.isOpened():
            self.cap.release()

# Create a window and pass it to the WebcamApp class
root = tk.Tk()
app = WebcamApp(root, "Tkinter Webcam Integration")
