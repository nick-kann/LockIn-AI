import tkinter as tk
from tkinter import ttk

class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        label = ttk.Label(self, text="Welcome to Your App", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        
        # Styling for the buttons
        style = ttk.Style()
        style.configure('Main.TButton', font=('Lato', 30))
        
        # Button 1: FOCUS MODE
        button1 = ttk.Button(self, text="FOCUS MODE", style='Main.TButton',
                            command=lambda: controller.show_frame("WebcamPage"))
        button1.pack(pady=20, padx=50, ipadx=10, ipady=10, fill='x')
        
        # Button 2: GRAPH YOUR FOCUS
        button2 = ttk.Button(self, text="GRAPH YOUR FOCUS", style='Main.TButton',
                            command=lambda: controller.show_frame("GraphPage"))
        button2.pack(pady=20, padx=50, ipadx=10, ipady=10, fill='x')
        
        # Button 3: OVERLAY MODE
        button3 = ttk.Button(self, text="OVERLAY MODE", style='Main.TButton',
                            command=lambda: controller.show_frame("OverlayPage"))
        button3.pack(pady=20, padx=50, ipadx=10, ipady=10, fill='x')
