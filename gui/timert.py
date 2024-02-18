import tkinter as tk
from tkinter import ttk
import cv2
from PIL import Image, ImageTk
import threading
import time

class TimerT():
    def __init__(self, container, btn_timer):
        self.container = container

        self.btn_timer = btn_timer
        #self.btn_set_timer = btn_set_timer
        

        self.timer_on = False
        self.timer_paused = False
        self.timer_start_time = None

        self.total_time_paused = 0

    def set_label(self, timer_label):
       self.timer_label = timer_label

    def get_label(self):
        return self.timer_label

    def timer_btn_press(self):
        # If the timer rn is running
        if self.timer_on:
            self.stop_timer()
        else:
            self.start_timer()

    def update_timer(self):
        if not self.timer_start_time:
            return
        elapsed_time = time.time() - self.timer_start_time - self.total_time_paused
        remaining_time = 1500 - elapsed_time
        hours, remainder = divmod(remaining_time, 3600)
        minutes, seconds = divmod(remainder, 60)
        milliseconds = (seconds - int(seconds)) * 1000
        
        time_text = ""
        
        if int(hours) != 0:
            time_text += f"{int(hours)} hr "
        if int(minutes) != 0:
            time_text += f"{int(minutes)} min "
        
        time_text += f"{int(seconds)} s"
            
        
        self.timer_label.configure(text=time_text)

    def start_timer(self):

        self.timer_on = True
        self.timer_start_time = time.time()
        self.btn_timer.configure(text="Stop Timer")

        # Create the Timer Pause Button
        self.btn_timer_pause = ttk.Button(self.container, text="Pause Timer", command=self.pause_timer)
        self.btn_timer_pause.pack(side=tk.LEFT, padx=5, pady=5)
        self.timer_paused = False

    def stop_timer(self):
        self.timer_on = False
        self.btn_timer.configure(text="Start Timer")
        self.btn_timer_pause.destroy()

        self.timer_label.configure(text="Timer Text")

        self.total_time_paused = 0



    def pause_timer(self):
        print("asfd")
        self.timer_paused = True
        self.time_when_paused = time.time()
        self.btn_timer_pause.configure(text="Unpause Timer", command=self.unpause_timer)

    def unpause_timer(self):
        self.timer_paused = False
        self.btn_timer_pause.configure(text="Pause Timer", command=self.pause_timer)
        self.total_time_paused += time.time() - self.time_when_paused


    def set_timer(self):
        pass
