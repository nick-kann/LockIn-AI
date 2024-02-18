import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from PIL import Image, ImageTk

class StartPage(ctk.CTkFrame):

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        
        img = Image.open('imgs/logo.png')
        photo = ImageTk.PhotoImage(img)

        # Create an image label widget and pack it at the top
        image_label = ctk.CTkLabel(self)
        image_label.configure(image=photo,text="")
        image_label.pack(pady=20)

        button1 = ctk.CTkButton(self, width = 210, height = 50, font = ('Lato', 20, 'bold'), text_color="white", text="FOCUS MODE", command=lambda: controller.show_frame("WebcamPage"), fg_color="#9B9999", hover_color="#676767")
        button1.pack(pady=20)
        button2 = ctk.CTkButton(self,width = 210, height = 50,font = ('Lato', 20, 'bold'), text_color="white", text="GRAPH YOUR FOCUS", command=lambda: controller.show_frame("GraphPage"), fg_color="#9B9999", hover_color="#676767")
        button2.pack(pady=20)

        button3 = ctk.CTkButton(self,width = 210, height = 50,font = ('Lato', 20, 'bold'), text_color="white", text="OVERLAY MODE", command=lambda: controller.show_frame("OverlayPage"), fg_color="#9B9999", hover_color="#676767")
        button3.pack(pady=20)
        
        button1.pack()
        button2.pack()
        button3.pack()

