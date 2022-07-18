import pytube
from tkinter import messagebox
import os
from sys import platform


class YouTube:
    def __init__(self, url, mp3):
        user = os.path.expanduser("~")
        if platform == "darwin":
            os.chdir(f"{user}/Downloads")
        elif platform == "win32":
            os.chdir(f"{user}\Downloads")
        self.yt = pytube.YouTube(url=url, use_oauth=False, allow_oauth_cache=True)
        self.video_title = self.yt.title
        self.audio_only = mp3
        self.check_vid_or_audio()

    def check_vid_or_audio(self):
        if self.audio_only:
            is_this_the_one = messagebox.askquestion(message=f"Is this the video name: \n{self.video_title}")
            if is_this_the_one == "yes":
                streams = self.yt.streams.filter(only_audio=True, mime_type="audio/mp4")
                download = streams.last()
                download.download()
        else:
            self.check_if_video()

    def check_if_video(self):
        is_this_the_one = messagebox.askquestion(message=f"Is this the video name: \n{self.video_title}")
        if is_this_the_one == "yes":
            stream = self.yt.streams.filter(progressive=True)
            download = stream.get_highest_resolution()
            download.download()

