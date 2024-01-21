import tkinter as tk
from tkinter import PhotoImage
from PIL import Image, ImageTk

def on_button_click():
    pass  # Add your button click logic here

# Create the main window
window = tk.Tk()
window.geometry("1600x900")
window.title("Pag-Ibig Form")

# Load the background image
background_image = PhotoImage(file="homebackground.png")

# Create a Canvas widget
canvas = tk.Canvas(window, width=1600, height=900)
canvas.pack()

# Set the background image
canvas.create_image(0, 0, anchor=tk.NW, image=background_image)

# Create other widgets (labels, entry fields, buttons, etc.)
label = tk.Label(window, text="Enter your name:")
entry = tk.Entry(window)
button = tk.Button(window, text="Submit", command=on_button_click)

# Place widgets on the Canvas or directly in the window
label.place(x=20, y=50)
entry.place(x=150, y=50)
button.place(x=150, y=80)

# Start the main event loop
window.mainloop()
