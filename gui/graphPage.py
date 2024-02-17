import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import threading

class graphPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # Button frame setup
        self.button_frame = ttk.Frame(self)
        self.button_frame.pack(fill=tk.X, side=tk.BOTTOM, expand=True)
        
        # Buttons setup
        self.btn_start = ttk.Button(self.button_frame, text="Start Webcam", command=self.meow)
        self.btn_start.pack(side=tk.LEFT, padx=5, pady=5)
        
        self.btn_stop = ttk.Button(self.button_frame, text="Stop Webcam", command=self.meow)
        self.btn_stop.pack(side=tk.LEFT, padx=5, pady=5)

        self.btn_stop = ttk.Button(self.button_frame, text="Button 3", command=self.meow)
        self.btn_stop.pack(side=tk.LEFT, padx=5, pady=5)
        
        self.btn_stop = ttk.Button(self.button_frame, text="Exit", command=lambda: controller.show_frame("StartPage"))
        self.btn_stop.pack(side=tk.LEFT, padx=5, pady=5)

        # Image setup
        self.img = ImageTk.PhotoImage(Image.open("./imgs/graph.png"))  # Keep reference to the image
        self.image_frame = tk.Frame(self, width=640, height=480)
        self.image_frame.pack(padx=10, pady=10, expand=True)
        
        # Label for image display
        label = tk.Label(self.image_frame, image=self.img)
        label.pack(expand=True)  # Center the label within image_frame

    def meow(self):
        print("meow")

