import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from PIL import Image, ImageTk
import threading
import matplotlib.pyplot as plt
import numpy as np
import os

class GraphPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.filepath = tk.StringVar()  # Variable to hold the filepath\

        """
        file_label = tk.Label(self, textvariable=self.filepath)  # Label to display the selected file path
        file_label.pack(pady=(0, 20))
        """

        self.button_frame = ttk.Frame(self)
        self.button_frame.pack()

        file_button = ttk.Button(self.button_frame, text="Select a file", style='Main.TButton', command=self.select_file)
        file_button.pack()
        
        button = ttk.Button(self.button_frame, text="Go to the start page", style='Main.TButton',
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()

    def select_file(self):
        """Open a file dialog for .lia files and update the filepath label with the selected file's path."""
        filename = filedialog.askopenfilename(
            filetypes=[("LIA Files", "*.lia")]  # Only allow .lia files
        )
        if filename:  # If a file was selected
            self.filepath.set(filename)  # Update the filepath variable
            self.print_file_contents(filename)  # Print the contents of the file

    def print_file_contents(self, filepath):
        """Open and print the contents of the specified file."""
        try:
            with open(filepath, 'r') as file:
                #contents = file.read()
                #print(contents)  # Print the contents to the console

                zero_count = 0
                one_count = 0
                for line in file:
                    if int(line) == 0:
                        zero_count += 1
                    elif int(line) == 1:
                        one_count += 1

                #print(zero_count)
                #print(one_count)

                sizes = [zero_count, one_count]
                labels = ['focused', 'unfocused']
                colors = ['gold', 'lightskyblue']
                explode = (0.1, 0) 

                plt.pie(sizes, explode=explode, labels=labels, colors=colors,
                autopct='%1.1f%%', shadow=True, startangle=140)
        
                plt.axis('equal')
                plt.savefig("pie_chart.png")  # Save the figure
                plt.close()  # Close the plot to free memory

                img = Image.open('pie_chart.png')
                photo = ImageTk.PhotoImage(img)
                original_width, original_height = img.size
                aspect_ratio = original_width / original_height
                new_height = 250
                new_width = int(new_height * aspect_ratio)

                img = img.resize((new_width, new_height))
                
                self.image_label = tk.Label(self)  # Label to display the pie chart image
                self.image_label.pack(pady=(10, 20))

                self.image_label.configure(image=photo)
                self.image_label.image = photo  # Keep a reference!


        except Exception as e:
            print(f"Failed to read file {filepath}: {e}")
