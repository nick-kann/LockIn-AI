import tkinter as tk   

class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is the start page", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(self, text="Focus Mode",
                            command=lambda: controller.show_frame("WebcamPage"))
        button2 = tk.Button(self, text="Go to Page Two",
                            command=lambda: controller.show_frame("graphPage"))
        button1.pack()
        button2.pack()
