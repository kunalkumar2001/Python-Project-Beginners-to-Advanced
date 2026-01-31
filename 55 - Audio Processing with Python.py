from pydub import AudioSegment
import urllib.request
import os

AudioSegment.converter = r"C:\ffmpeg\bin\ffmpeg.exe"


urllib.request.urlretrieve("https://tinyurl.com/wx9amev", "loop.wav")
urllib.request.urlretrieve("https://tinyurl.com/yx3k5kw5", "beat.wav")

loop = AudioSegment.from_wav("loop.wav")
beat = AudioSegment.from_wav("beat.wav")

loop2 = loop * 2
length = len(loop2)

# Trim beat to same length & reduce volume
beat = beat[:length] - 6   # reduce beat volume by 6 dB
loop2 = loop2 - 2          


mixed = beat.overlay(loop2)

fade_time = int(length * 0.3)
final_mix = mixed.fade_in(fade_time).fade_out(fade_time)


final_mix.export("final_mix.wav", format="wav")


os.startfile("final_mix.wav")
