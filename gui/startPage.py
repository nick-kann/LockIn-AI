import tkinter as tk
from tkinter import ttk
import customtkinter as ctk

class StartPage(ctk.CTkFrame):

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        
        # label = ctk.CTkLabel(self, text="FAT", font=controller.title_font)
        # label.pack(side="top", fill="x", pady=10)

        button_style = {"foreground": "white"}

        button1 = ctk.CTkButton(self, width = 210, height = 50, font = ('Lato', 20, 'bold'), text_color="white", text="FOCUS MODE", command=lambda: controller.show_frame("WebcamPage"), fg_color="#9B9999", hover_color="#676767")
        button1.pack(pady=20)
        button2 = ctk.CTkButton(self,width = 210, height = 50,font = ('Lato', 20, 'bold'), text_color="white", text="GRAPH YOUR FOCUS", command=lambda: controller.show_frame("GraphPage"), fg_color="#9B9999", hover_color="#676767")
        button2.pack(pady=20)

        button3 = ctk.CTkButton(self,width = 210, height = 50,font = ('Lato', 20, 'bold'), text_color="white", text="OVERLAY MODE", command=lambda: controller.show_frame("OverlayPage"), fg_color="#9B9999", hover_color="#676767")
        button3.pack(pady=20)
        
        button1.pack()
        button2.pack()
        button3.pack()

