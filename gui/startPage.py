import tkinter as tk   
import ttkbootstrap as ttk

class StartPage(tk.Frame):

    def __init__(self,  parent, controller):
        tk.Frame.__init__(self, parent )
        self.controller = controller
        label = ttk.Label(self, text="This is the start page", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        button1 = ttk.Button(self, text="Focus Mode", bootstyle="outline",
                            command=lambda: controller.show_frame("WebcamPage"))
        button2 = ttk.Button(self, text="Graph your focus", bootstyle="outline", 
                            command=lambda: controller.show_frame("graphPage"))
        button3 = ttk.Button(self, text="Overlay Mode", bootstyle="outline",
                            command=lambda: controller.show_frame("OverlayPage"))
        button1.pack()
        button2.pack()
        button3.pack()

