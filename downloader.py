import os
from pytube import YouTube, exceptions
from time import time
from _tkinter import *
from customtkinter import *

# set-up
set_appearance_mode("System") #set up the appearance to follow the system settings: "system", "light", "dark"
set_default_color_theme("blue")
for item in os.listdir(os.getcwd()):
    if item == "youtube_downloads": #if there is a folder already, do not create a new one
        break
else:
    os.mkdir("youtube_downloads") #create a folder if there was no folder

def download_video(entry_field):
    """_summary_

    Args:
        entry_field (_type_): _description_
    """
    try:
        initial_time = time()
        location = "youtube_downloads/"
        YouTube(entry_field).streams.first().downloads(location)
        final_time = time()

        #interface
        screen = CTk()
        screen.title("Download Status")
        screen.resizable(False, False)
        screen.geometry("200x100")
        screen.grid_columnconfigure(0, weight=1)
        screen.grid_rowconfigure((0,1), weight=1)
        message = StringVar()
        message.set(f"Download Successfull!\nTotal time taken: {round(final_time-initial_time,3)} seconds")
        on_screen = CTkLabel(screen, text=message.get())
        on_screen.grid(row=0, column=0)
        button = CTkButton(screen, text="OK", command=screen.destroy)
        button.grid(row=1, column=0)
        screen.mainloop()
    except exceptions.RegexMatchError:#this is for an error message
        error_message = CTk()
        error_message.title("Error")
        error_message.resizable(False, False)
        error_message.geometry("300x100")
        error_message.grid_rowconfigure((0,1), weight=1)
        error_message.grid_columnconfigure(0, weight=1)
        error_label = CTkLabel(error_message, text="Please Enter a Valid YouTube link")
        error_label.grid(row=0, column=0)
        button = CTkButton(error_message, text="OK", command=error_message.destroy)
        button.grid(row=1, column=0)
        error_message.mainloop()

#layout of the app
layout = CTk()
layout.title("<i> Download From YouTube")
layout.grid_rowconfigure((0,1), weight=1)
layout.grid_columnconfigure((0,1), weight=1)
layout.geometry("350x150")
layout.resizable(False, False)
CTkLabel(layout, text="Paste URL From YouTube").grid(row=0, column=0)
entry = CTkEntry(layout)
entry.grid(row=0, column=1)
CTkButton(layout, text='Download', command=lambda*args: download_video(entry.get())).grid(row=1, column=0, columnspan = 2)
layout.mainloop()

