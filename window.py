import tkinter as tk
from tkinter import filedialog as fd
from logic import YouTube
from tkinter import messagebox
import os


class Window:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Youtube Downloader by KillSamurai!")

        self.URL = tk.StringVar()
        self.VIDEO_MP3 = tk.StringVar()
        self.path_label = tk.StringVar()


        uri = tk.Label(self.root, text="YouTube URL: ")
        url = tk.Entry(self.root, textvariable=self.URL)
        self.saved_path = os.getcwd()

        uri.grid(column=0, row=0, padx=10, pady=10)
        url.grid(column=1, row=0, padx=10, pady=10)

        video = tk.Radiobutton(self.root, text="Video", variable=self.VIDEO_MP3, value=False)
        mp3 = tk.Radiobutton(self.root, text="Audio Only", variable=self.VIDEO_MP3, value=True)

        mp3.select()

        mp3.grid(column=1, row=1, padx=10, pady=10)
        video.grid(column=0, row=1, padx=10, pady=10)

        self.path_label = tk.Entry(self.root, textvariable=self.path_label)
        self.path_label.grid(column=0, row=2, padx=10, pady=10)
        self.path_label.insert(0, self.saved_path)

        self.browse = tk.Button(self.root, text="Browse folder", command=lambda: self.where_to_save())
        self.browse.grid(column=1, row=2, padx=10, pady=10)

        button = tk.Button(self.root, text="LET'S GOOOO!!!!", command=lambda: self.check_mandatory())
        button.grid(column=0, row=3, padx=10, pady=10, columnspan=3)

        self.root.mainloop()

    def initiate(self):
        yt_url = self.URL.get()
        mp3_video = self.VIDEO_MP3.get()
        YouTube(url=yt_url, mp3=mp3_video, path=self.saved_path)
        messagebox.showinfo(title="File Downloaded", message=f"File Downloaded at:\n {self.saved_path}")
        go_on = messagebox.askquestion(message="A New Video to download?")
        if go_on == "no":
            self.root.destroy()

    def check_mandatory(self):
        if self.URL.get():
            self.initiate()
        else:
            messagebox.showerror(title="ERROR", message="No URL in the URL BOX")

    def where_to_save(self):
        self.saved_path = fd.askdirectory(parent=self.root, initialdir=self.saved_path, title="Choose where to save")
        self.path_label.insert(0, self.saved_path)
