import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import threading
from tkinter import filedialog

class GraphPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.filepath = tk.StringVar()  # Variable to hold the filepath\

        """
        file_label = tk.Label(self, textvariable=self.filepath)  # Label to display the selected file path
        file_label.pack(pady=(0, 20))
        """
        
        file_button = ttk.Button(self, text="Select a file", style='Main.TButton', command=self.select_file)
        file_button.pack()
        
        button = ttk.Button(self, text="Go to the start page", style='Main.TButton',
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()

    def select_file(self):
        """Open a file dialog and update the filepath label with the selected file's path."""
        filename = filedialog.askopenfilename()  # Open the file dialog
        if filename:  # If a file was selected
            self.filepath.set(filename)  # Update the filepath variable
