import PyPDF2
import pyttsx3

engine = pyttsx3.init()

full_text = ""

file = open("file.pdf", "rb")
pdfReader = PyPDF2.PdfReader(file)

for page in pdfReader.pages:
    text = page.extract_text()
    if text:
        full_text += text + "\n"
        engine.say(text)
        engine.runAndWait()

# Save to audio file
engine.save_to_file(full_text, "audio.mp3")
engine.runAndWait()

engine.stop()
file.close()
