import tkinter as tk

class RoundedButton(tk.Canvas):
    def __init__(self, parent, width, height, corner_radius, **kwargs):
        tk.Canvas.__init__(self, parent, width=width, height=height, highlightthickness=0)
        self.command = kwargs.pop("command", None)
        
        # Draw rounded rectangle
        self.create_oval((0, 0, corner_radius*2, corner_radius*2), fill="blue", outline="blue")
        self.create_oval((width - corner_radius*2, 0, width, corner_radius*2), fill="blue", outline="blue")
        self.create_oval((0, height - corner_radius*2, corner_radius*2, height), fill="blue", outline="blue")
        self.create_oval((width - corner_radius*2, height - corner_radius*2, width, height), fill="blue", outline="blue")
        self.create_rectangle((0, corner_radius, width, height - corner_radius), fill="blue", outline="blue")
        self.create_rectangle((corner_radius, 0, width - corner_radius, height), fill="blue", outline="blue")

        # Add clickable label over the canvas
        self.label = tk.Label(self, text=kwargs.get("text", ""), bg="blue", fg="white")
        self.label.place(x=corner_radius, y=corner_radius, width=width - corner_radius*2, height=height - corner_radius*2)
        
        self.bind("<Button-1>", self._on_click)

    def _on_click(self, event):
        if self.command:
            self.command()

def my_command():
    print("Button clicked!")

root = tk.Tk()
button = RoundedButton(root, width=120, height=40, corner_radius=10, text="Click Me!", command=my_command)
button.pack(pady=20)
root.mainloop()

