import os
import subprocess
import tkinter as tk
from tkinter import filedialog

def add_subtitles(video_file, subtitle_file):
    output_dir = os.path.dirname(video_file)
    output_file = os.path.join(output_dir, "output_soft_english.mp4")
    command = [
        "ffmpeg",
        "-i",
        video_file,
        "-i",
        subtitle_file,
        "-c:v",
        "copy",
        "-c:a",
        "copy",
        "-c:s",
        "mov_text",
        "-metadata:s:s:0",
        "language=ara",
        "-map",
        "0",
        "-map",
        "-s",
        "-map",
        "1",
        output_file
    ]

    subprocess.run(command)
    print("Subtitles added successfully!")





def select_video_file():
    root = tk.Tk()
    root.withdraw()
    video_file = filedialog.askopenfilename(filetypes=[("Video Files", "*.mp4;*.mkv")])
    return video_file

def select_subtitle_file():
    root = tk.Tk()
    root.withdraw()
    subtitle_file = filedialog.askopenfilename(filetypes=[("Subtitle Files", "*.srt;*.ass")])
    return subtitle_file

video_file = select_video_file()
subtitle_file = select_subtitle_file()

if video_file and subtitle_file:
    add_subtitles(video_file, subtitle_file)
else:
    print("Video or subtitle file not selected.")
