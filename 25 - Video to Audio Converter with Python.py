import tkinter as tk
from tkinter import messagebox, filedialog
import subprocess
import os
import sys
import shutil
from pytube import YouTube
import pytube.extract

def find_ffmpeg():
    base_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
    bundled = os.path.join(
        base_dir,
        "ffmpeg-master-latest-win64-gpl",
        "bin",
        "ffmpeg.exe"
    )
    if os.path.isfile(bundled):
        return bundled
    if shutil.which("ffmpeg"):
        return "ffmpeg"
    return None


def download_audio():
    url = url_entry.get().strip()
    if not url:
        messagebox.showerror("Error", "Enter a YouTube URL")
        return

    status_var.set("Extracting video ID...")
    root.update()

    try:
        video_id = pytube.extract.video_id(url)
    except Exception as e:
        messagebox.showerror("Error", f"Invalid YouTube URL\n{e}")
        return

    ffmpeg = find_ffmpeg()
    if not ffmpeg:
        messagebox.showerror(
            "Error",
            "ffmpeg not found.\nInstall ffmpeg or place it in the bundled folder."
        )
        return

    try:
       
        status_var.set("Downloading audio with yt-dlp...")
        root.update()

        ytdlp_cmd = [
            sys.executable, "-m", "yt_dlp",
            "-x",
            "--audio-format", "mp3",
            "-o", f"{video_id}.%(ext)s",
            url
        ]
        subprocess.run(ytdlp_cmd, check=True)

        # Find output file
        downloaded_file = None
        for f in os.listdir():
            if f.startswith(video_id):
                downloaded_file = os.path.abspath(f)
                break

        if not downloaded_file:
            raise Exception("Download finished but file not found.")

        if downloaded_file.lower().endswith(".mp3"):
            status_var.set("Download completed successfully.")
            messagebox.showinfo("Success", f"Saved MP3:\n{downloaded_file}")
            return

    except Exception:
        
        try:
            status_var.set("yt-dlp failed. Using pytube...")
            root.update()

            yt = YouTube(url)
            stream = yt.streams.filter(only_audio=True).order_by("abr").desc().first()
            if not stream:
                raise Exception("No audio stream available.")

            downloaded_file = stream.download(filename=video_id)
        except Exception as e:
            messagebox.showerror("Error", f"Download failed\n{e}")
            return

    
    status_var.set("Converting to MP3...")
    root.update()

    base, _ = os.path.splitext(downloaded_file)
    mp3_path = base + ".mp3"

    cmd = [
        ffmpeg, "-y",
        "-i", downloaded_file,
        "-vn",
        "-b:a", "192k",
        "-ar", "44100",
        mp3_path
    ]

    try:
        subprocess.run(cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        os.remove(downloaded_file)
        status_var.set("Conversion completed.")
        messagebox.showinfo("Success", f"Saved MP3:\n{mp3_path}")
    except subprocess.CalledProcessError as e:
        messagebox.showerror(
            "FFmpeg Error",
            e.stderr.decode("utf-8", errors="ignore")
        )


root = tk.Tk()
root.title("YouTube to MP3 Downloader")
root.geometry("520x220")
root.resizable(False, False)

tk.Label(root, text="YouTube URL", font=("Segoe UI", 11)).pack(pady=10)

url_entry = tk.Entry(root, width=65)
url_entry.pack(pady=5)

download_btn = tk.Button(
    root,
    text="Download MP3",
    font=("Segoe UI", 11),
    command=download_audio
)
download_btn.pack(pady=15)

status_var = tk.StringVar(value="Idle")
status_label = tk.Label(
    root,
    textvariable=status_var,
    fg="blue",
    font=("Segoe UI", 10)
)
status_label.pack(pady=5)

root.mainloop()
