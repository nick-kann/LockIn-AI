import tkinter as tk

class OverlayPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Overlay Mode Page", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Start Page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()

        self.resize_application_window(800, 600)  # Example size: 800x600

    def resize_application_window(self, width, height):
        # Assuming 'controller' has access to the main application window
        self.controller.geometry(f"{width}x{height}")