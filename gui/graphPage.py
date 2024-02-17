import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import threading

class graphPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.controller = controller

        # Create a frame for the buttons
        self.button_frame = ttk.Frame(self)
        self.button_frame.pack(fill=tk.X, side=tk.BOTTOM, expand=True)
        
        # Buttons
        self.btn_start = ttk.Button(self.button_frame, text="Start Webcam", command=exit)
        self.btn_start.pack(side=tk.LEFT, padx=5, pady=5)
        
        self.btn_stop = ttk.Button(self.button_frame, text="Stop Webcam", command=exit)
        self.btn_stop.pack(side=tk.LEFT, padx=5, pady=5)

        # Create the Stop Webcam button
        self.btn_stop = ttk.Button(self.button_frame, text="Button 3", command=exit)
        self.btn_stop.pack(side=tk.LEFT, padx=5, pady=5)
        
        # Create the Stop Webcam button
        self.btn_stop = ttk.Button(self.button_frame, text="Exit", command=exit)
        self.btn_stop.pack(side=tk.LEFT, padx=5, pady=5)

        img = ImageTk.PhotoImage(Image.open("./imgs/graph.png"))
        self.image_frame = tk.Frame(self, width=640, height=480)
        self.image_frame.pack(padx=10, pady=10, expand=True)
        self.image_frame.place(anchor='center', relx=0.5, rely=0.5)

        label = tk.Label(self.image_frame, image = img)
        label.pack()

    
