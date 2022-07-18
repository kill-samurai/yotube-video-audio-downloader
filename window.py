import tkinter as tk
from logic import YouTube
from tkinter import messagebox


class Window:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Youtube Downloader by KillSamurai!")
        self.URL = tk.StringVar()
        self.VIDEO_MP3 = tk.StringVar()
        self.PERCENTAGE = "0%"
        uri = tk.Label(self.root, text="YouTube URL: ")
        url = tk.Entry(self.root, textvariable=self.URL)

        uri.grid(column=0, row=0, padx=10, pady=10)
        url.grid(column=1, row=0, padx=10, pady=10)

        mp3 = tk.Radiobutton(self.root, text="Audio Only", variable=self.VIDEO_MP3, value=f"only_audio={True}")
        video = tk.Radiobutton(self.root, text="Video", variable=self.VIDEO_MP3, value=f"only_video={True}")

        mp3.grid(column=0, row=1, padx=10, pady=10)
        # video.grid(column=1, row=1, padx=10, pady=10)

        percentage_label = tk.Label(self.root, text=self.PERCENTAGE)
        # percentage_label.grid(column=0, row=2, pady=10, padx=10, columnspan=3)

        button = tk.Button(self.root, text="LET'S GOOOO!!!!", command=lambda: self.check_mandatory())
        button.grid(column=0, row=3, padx=10, pady=10, columnspan=3)

        self.root.mainloop()

    def initiate(self):
        yt_url = self.URL.get()
        mp3_video = self.VIDEO_MP3.get()
        YouTube(url=yt_url, mp3=mp3_video)

        go_on = messagebox.askquestion(message="Continue?")
        if go_on == "no":
            self.root.destroy()

    def check_mandatory(self):
        if self.URL.get():
            self.initiate()
        else:
            messagebox.showerror(title="No URL", message="No URL in the URL BOX")








