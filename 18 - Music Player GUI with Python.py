import os
from tkinter import *
from PIL import Image, ImageTk
from pygame import mixer




#colors
col1 = '#ffffff'
col2 = '#3C1dc6'
col3 = '#333333'
col4 = "#C7E3F8"
col5 = "#2781A7"
col6 = "#A8D5E8"

window = Tk()
window.title('Music Player')
window.geometry('400x300')
window.configure(bg=col1)
window.resizable(width=FALSE, height=FALSE)

#events
def play_music():
    running = listbox.get(ACTIVE)
    running_song['text'] = running
    mixer.music.load(running)
    mixer.music.play()
    
    
def pause_music():
    mixer.music.pause()
    
def continue_music():
    mixer.music.unpause()
    
def stop_music():
    mixer.music.stop()  
    
def next_music():
    playing = running_song['text']
    index = songs.index(playing) 
    new_index = index + 1
    playing = songs[new_index]
    mixer.music.load(playing)
    mixer.music.play()
    
    listbox.delete(0, END)

    show()
    listbox.select_set(new_index)
    running_song['text'] = playing


def previous_music():
    playing = running_song['text']
    index = songs.index(playing) 
    new_index = index - 1
    playing = songs[new_index]
    mixer.music.load(playing)
    mixer.music.play()
    
    listbox.delete(0, END)

    show()
    listbox.select_set(new_index)
    running_song['text'] = playing       




#frames
left_frame = Frame(window, width = 150, height=150, bg=col1)
left_frame.grid(row=0, column=0, padx=0, pady=0, sticky=NSEW)

right_frame = Frame(window, width = 250, height=150, bg=col3)
right_frame.grid(row=0, column=1, padx=(1,0), pady=0, sticky=NSEW)

right_frame.grid_propagate(False)

right_frame.grid_rowconfigure(0, weight=1)
right_frame.grid_columnconfigure(0, weight=1)  # content expands
right_frame.grid_columnconfigure(1, weight=0)  # scrollbar stays tight


down_frame = Frame(window, width = 400, height=200, bg=col4)
down_frame.grid(row=1, column=0, columnspan=3, padx=0, pady=0, sticky=NSEW)

#Right frame
listbox = Listbox(right_frame,bd=0, selectmode=SINGLE, font = ("arial 10 bold"), bg=col3, fg=col1)
listbox.grid(row=0, column=0, sticky=NSEW,padx=0, pady=0)

w = Scrollbar(right_frame, orient=VERTICAL, command=listbox.yview)
w.grid(row=0, column=1, sticky ='NS')

listbox.config(yscrollcommand=w.set)
w.config(command=listbox.yview)

#images
img_1 = Image.open('Icons/1.png')
img_1 = img_1.resize((130, 130))
img_1 = ImageTk.PhotoImage(img_1)
app_image = Label(left_frame, image=img_1, bg=col1)
app_image.place(relx=0.5, rely=0.60, anchor=CENTER)



img_2 = Image.open('Icons/2.png')
img_2 = img_2.resize((30, 30))
img_2 = ImageTk.PhotoImage(img_2)
play_button = Button(down_frame, image=img_2,padx=10 ,font=("Ivy 10"), width=50, height=50,bg=col6, command=play_music)
play_button.place(x=56+28, y=50)


img_3 = Image.open('Icons/3.png')
img_3 = img_3.resize((30, 30))
img_3 = ImageTk.PhotoImage(img_3)
prev_button = Button(down_frame, image=img_3,padx=10, bg=col6,font=("Ivy 10"), width=50, height=50, command=previous_music)
prev_button.place(x=10+28, y=50,)

img_4 = Image.open('Icons/4.png')
img_4 = img_4.resize((30, 30))
img_4 = ImageTk.PhotoImage(img_4)
next_button = Button(down_frame, image=img_4,padx=10, bg=col6,font=("Ivy 10"), width=50, height=50, command=next_music)
next_button.place(x=102+28, y=50,)

img_5 = Image.open('Icons/5.png')
img_5 = img_5.resize((30, 30))
img_5 = ImageTk.PhotoImage(img_5)
pause_button = Button(down_frame, image=img_5,padx=10, bg=col6,font=("Ivy 10"), width=50, height=50, command=pause_music)
pause_button.place(x=148+28, y=50,)

img_6 = Image.open('Icons/6.png')
img_6 = img_6.resize((30, 30))
img_6 = ImageTk.PhotoImage(img_6)
continue_button = Button(down_frame, image=img_6,padx=10, bg=col6,font=("Ivy 10"), width=50, height=50, command=continue_music)
continue_button.place(x=194+28, y=50,)

img_7 = Image.open('Icons/7.png')
img_7 = img_7.resize((30, 30))
img_7 = ImageTk.PhotoImage(img_7)
stop_button = Button(down_frame, image=img_7,padx=10, bg=col6,font=("Ivy 10"), width=50, height=50, command=stop_music,)
stop_button.place(x=240+28, y=50,)



line = Label(left_frame,bg=col3,height=1,width=150)
line.place(x=0, y=1)

running_song = Label(down_frame, text = "Choose a song",font = ("Ivy", 10,"bold"), width = 100, height=2, bg= col5,fg= col3)
running_song.place(relx=0.5, rely=0.1, anchor="center")

#events
def play_music():
    running = listbox.get(ACTIVE)
    running_song['text'] = running
    mixer.music.load(running)
    mixer.music.play()







os.chdir(r"D:\Complete Python\Project\Python Project\Music")
songs = os.listdir()

def show():
    for song in songs:
        listbox.insert(END, song)

show()


mixer.init()
music_state = StringVar()
music_state.set("Choose One!")


window.mainloop()