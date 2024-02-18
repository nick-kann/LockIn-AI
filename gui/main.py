import tkinter as tk                # python 3
from tkinter import font as tkfont  # python 3
from webcamPage import WebcamPage
from startPage import StartPage
from graphPage import GraphPage
from pageOne import PageOne
from pageTwo import PageTwo
from overlayPage import OverlayPage
import ttkbootstrap as ttkb
from ttkbootstrap.constants import *
import customtkinter as ctk

class SampleApp(ttkb.Window):

    def __init__(self,  *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
           
        self.title("LockInAI")
        self.title_font = ctk.CTkFont(family='Helvetica', size=18, weight="bold", slant="italic")
        ctk.set_default_color_theme("./gui/theme.json")  # Themes: "blue" (standard), "green", "dark-blue"

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = ctk.CTkFrame(self )
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        

        self.frames = {}
        for F in (StartPage, PageOne, PageTwo, WebcamPage, GraphPage, OverlayPage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")
        
       

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''

        if page_name=="OverlayPage":
            screen_width = self.winfo_screenwidth()  # Get the width of the screen
            self.geometry(f"{screen_width}x100")  # Set window width to screen width and height to 600
            
            self.attributes('-topmost', True)  # Keep window always on top
        else:
            self.geometry("")  # Reset to default size
            self.attributes('-topmost', False)  # No longer keep window always on top

        frame = self.frames[page_name]
        frame.tkraise()


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
