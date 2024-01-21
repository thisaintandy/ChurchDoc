import tkinter as tk
from tkinter import PhotoImage

class ChurchDocApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("1350x750")
        self.title("ChurchDoc App")
        self.resizable(width=False, height=False)

        # Create a frame for pages
        self.page_frame = tk.Frame(self)
        self.page_frame.place(relwidth=1, relheight=1)

        # Load the images
        self.homebackground_image = PhotoImage(file="homebackground.png")
        self.request_image = PhotoImage(file="requestbutton.png")
        self.appoint_image = PhotoImage(file="appointbutton.png")
        self.request_background_image = PhotoImage(file="requestbackground.png")
        self.appoint_background_image = PhotoImage(file="appointbackground.png")
        self.logo_image = PhotoImage(file="logo.png")
        # Initialize the main window with the home background
        self.show_home_page()

    def initialize_buttons(self):
        # Create buttons on the page frame
        self.logo_button = tk.Button(self.page_frame,command=self.show_home_page,image=self.logo_image,bd=0, relief=tk.FLAT, 
        highlightthickness=-1, highlightbackground="brown", highlightcolor="brown")
        self.logo_button.place(x=0, y=15)
        
        self.request_button = tk.Button(self.page_frame, command=self.show_request_page, image=self.request_image, bd=0)
        self.request_button.place(x=825, y=695)

        self.appoint_button = tk.Button(self.page_frame, command=self.show_appoint_page, image=self.appoint_image, bd=0)
        self.appoint_button.place(x=1075, y=695)

    def show_home_page(self):
        self.page_frame.destroy()
        self.page_frame = tk.Frame(self)
        self.page_frame.place(relwidth=1, relheight=1)

        # Set the background image for the main window
        canvas = tk.Canvas(self.page_frame, width=1600, height=900)
        canvas.pack()
        canvas.create_image(0, 0, anchor=tk.NW, image=self.homebackground_image)

        self.initialize_buttons()

    def show_request_page(self):
        self.page_frame.destroy()
        self.page_frame = tk.Frame(self)
        self.page_frame.place(relwidth=1, relheight=1)

        # Set the background image for the request page
        canvas = tk.Canvas(self.page_frame, width=1600, height=900)
        canvas.pack()
        canvas.create_image(0, 0, anchor=tk.NW, image=self.request_background_image)

        self.initialize_buttons()

    def show_appoint_page(self):
        self.page_frame.destroy()
        self.page_frame = tk.Frame(self)
        self.page_frame.place(relwidth=1, relheight=1)

        # Add logic to show the Appoint page if needed
        # Set the background image for the Appoint page
        # Set the background image for the request page
        canvas = tk.Canvas(self.page_frame, width=1600, height=900)
        canvas.pack()
        canvas.create_image(0, 0, anchor=tk.NW, image=self.appoint_background_image)
        
        self.initialize_buttons()





if __name__ == "__main__":
    app = ChurchDocApp()
    app.mainloop()
