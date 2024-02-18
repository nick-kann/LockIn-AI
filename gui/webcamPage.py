import tkinter as tk
from tkinter import ttk
import cv2
from PIL import Image, ImageTk
import threading
import time
from timert import TimerT
import tensorflow as tf
from tensorflow.keras import layers, models, applications, losses
import numpy as np
from playsound import playsound
import datetime
from pygame import mixer


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
        self.btn_start.pack(side=tk.LEFT, padx=(310, 15), pady=5, ipadx=30)
        
        # self.btn_stop = ttk.Button(self.button_frame, text="Stop Webcam", command=self.stop_webcam)
        # self.btn_stop.pack(side=tk.LEFT, padx=5, pady=5)

        # Create the Stop Webcam button
        self.btn_stop = ttk.Button(self.button_frame, text="Exit", command=lambda: [self.sound.stop(), controller.show_frame("StartPage")])

        self.btn_stop.pack(side=tk.LEFT, padx=15, pady=5, ipadx=40)


        self.video_frame = tk.Frame(self, width=940, height=480)
        self.video_frame.pack(padx=15, pady=5, expand=True)

        # Adjustments to video label to place it inside video_frame
        self.video_label = tk.Label(self.video_frame, bd=15)
        self.video_label.pack()

        # Create the Start Timer Button
        self.btn_timer = ttk.Button(self.button_frame, text="Start Timer")
        self.btn_timer.pack(side=tk.LEFT, padx=15, pady=5, ipadx=30)
        
        """
        self.btn_set_timer = ttk.Button(self.button_frame, text="Set Timer")
        self.btn_set_timer.pack(side=tk.LEFT, padx=5, pady=5)
        """

        #self.timer = TimerT(self.button_frame, self.btn_timer, self.btn_set_timer)
        self.timer = TimerT(self.button_frame, self.btn_timer)
        self.btn_timer.config(command=self.timer.timer_btn_press)
        #self.btn_set_timer.config(command=self.timer.set_timer)

        self.timer_label = tk.Label(self.video_frame, text="Timer", bg="#B7EDE8", fg="black", relief="solid", bd=4)
        self.timer_label.place(relx=0.679, rely=0.027, relwidth=0.3, relheight=0.1)
        self.timer_label.config(bg="#B7EDE8")
        self.timer_label.config(fg="black")
        self.timer_label.config(font=("Lato", 20, "bold"))
        self.timer.set_label(self.timer_label)

        mixer.init()
        self.sound = mixer.Sound("unfocused-alarm.mp3")
        self.sound_playing = False
        
        self.frame_counter = 0
        
        saved_model_dir = "./saved_model"
        self.loaded_model = tf.saved_model.load(saved_model_dir)
        
        self.focuslist = []
        
        self.running = False
        self.update_frame()  # Start the update loop for the video frames


    def start_webcam(self):
        if not self.running:
            self.running = True
            self.btn_start.config(text="Stop Webcam")
            self.timer.get_label().config(bd=4)
            self.timer.get_label().config(font=("Lato", 20, "bold"))
            
            
            self.focus_label = tk.Label(self, text="FOCUSED", bg="white", relief="solid", bd=0)
            self.focus_label.config(fg="green")
            
            self.focus_label.place(relx=0.37, rely=0.7, relwidth=0.3, relheight=0.1)
            self.focus_label.config(font=("Lato", 30, "bold"))
            
            self.focustracker = []
            
        else:
            self.stop_webcam()
            self.sound.stop()
            self.btn_start.config(text="Start Webcam")
            self.running = False
            
            current_datetime = datetime.datetime.now()
            formatted_datetime = current_datetime.strftime("%Y-%m-%d %H-%M-%S" + ".lia")
            file_path = formatted_datetime
            with open(file_path, "w") as file:
                file.writelines([str(item) + "\n" for item in self.focustracker])
    
    def stop_webcam(self):
        self.timer.get_label().config(bd=4)
        self.timer.get_label().config(font=("Lato", 20, "bold"))
        self.running = False
        # Clear the video label
        self.video_label.config(image='')  # Clears the label
        # Optionally, you can set a placeholder text or a default image here
        self.video_label.config(text='Webcam stopped')  # Placeholder text
        # If setting a default image, you would do something like this:
        default_img = ImageTk.PhotoImage(Image.open("./imgs/istockphoto-945783206-612x612.jpg").resize((640, 480), Image.Resampling.HAMMING))
        self.video_label.imgtk = default_img
        self.video_label.config(image=default_img)
        self.focus_label.config(text="")

              
    
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
                
                self.frame_counter += 1
                if self.frame_counter >= 15:
                    self.frame_counter = 0
                    # converting pixel values (uint8) to float32 type
                    img = tf.cast(img, tf.float32)
                    # normalizing the data to be in range of -1, +1
                    img = applications.resnet_v2.preprocess_input(img)
                    # resizing all images to a shape of 224x*224*3
                    img = tf.image.resize(img, (224, 224))
                    img = img.numpy()
                    img = np.expand_dims(img, axis = 0)
                    predictions = self.loaded_model(img)
                    value = np.round(predictions[0, 0])
                    self.focuslist.append(value)
                    if (len(self.focuslist) > 10):
                        del self.focuslist[0]
                    focuscounter = 0
                    for i in self.focuslist:
                        focuscounter += i
                    if (focuscounter >= 8):
                        print("UNFOCUSED")
                        self.focustracker.append(1)
                        self.focus_label.config(text="UNFOCUSED")
                        self.focus_label.config(fg="red")
                        self.focus_label.place(relx=0.35)
                        if not mixer.get_busy():
                            self.sound.play()
                    else:
                        self.focustracker.append(0)
                        self.focus_label.config(text="FOCUSED")
                        self.focus_label.config(fg="green")
                        self.focus_label.place(relx=0.37)
                        self.sound.stop()
                        
                    
        else:
            default_img = ImageTk.PhotoImage(Image.open("./imgs/istockphoto-945783206-612x612.jpg").resize((640, 480), Image.Resampling.HAMMING))
            self.video_label.imgtk = default_img
            self.video_label.config(image=default_img)
        self.parent.after(10, self.update_frame)  # Repeat after an interval
        if self.timer.timer_on and (not self.timer.timer_paused):   
            self.timer.update_timer()

    def __del__(self):
        if self.cap.isOpened():
            self.cap.release()
