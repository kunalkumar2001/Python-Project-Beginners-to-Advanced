import whisper
import os
import numpy as np
import librosa
from moviepy.editor import VideoFileClip

video_file = "video.mp4"
audio_file = "audio.wav"

# Check if video file exists, if not try alternative paths
if not os.path.exists(video_file):
    if os.path.exists("Video/video.mp4"):
        video_file = "Video/video.mp4"
    else:
        raise FileNotFoundError(f"Video file not found. Tried: video.mp4, Video/video.mp4")

# 1. Convert video to audio using MoviePy
try:
    video = VideoFileClip(video_file)
    video.audio.write_audiofile(audio_file, verbose=False, logger=None)
    video.close()
except Exception as e:
    print(f"Error converting video: {e}")
    raise

# 2. Load Whisper model
model = whisper.load_model("base")

# 3. Load audio using librosa to avoid ffmpeg dependency in Whisper
audio, sr = librosa.load(audio_file, sr=16000)

# 3. Transcribe using pre-loaded audio
result = model.transcribe(
    audio,
    language="en",        # change to "hi" for Hindi
    verbose=False
)

# 4. Save transcription
with open("output.txt", "w", encoding="utf-8") as f:
    f.write(result["text"])

print("Transcription saved to output.txt")
