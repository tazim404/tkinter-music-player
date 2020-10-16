from tkinter import *
from tkinter import filedialog
import tkinter.messagebox as box
from tkinter.ttk import Progressbar
from pygame import mixer
from mutagen.mp3 import MP3
window = Tk()
window.title("Music Player")
window.resizable(False, False)
icon_image = PhotoImage(file='icon.png')
window.iconphoto(True, icon_image)
mixer.init()
muted = False


def voice(vol):
    volu = int(vol)/100
    mixer.music.set_volume(volu)


def stop():
    mixer.music.stop()


paused = False


def pause():
    global paused
    if paused == True:
        paused = False
        mixer.music.unpause()
    else:
        paused = True
        mixer.music.pause()


def about():
    box.showinfo("About", "This music player is created by Tazmi Rahbar")


muted = False


def mute():
    global muted
    if muted == True:
        mixer.music.set_volume(0)
        sound_bar.set(0)
        muted = False
    elif muted == False:
        mixer.music.set_volume(50)
        sound_bar.set(50)
        muted = True


def add():
    global filename
    filename = filedialog.askopenfilename()
    list_box.insert(END, filename)


def play():
    try:
        selectd_song = list_box.get(list_box.curselection())
        print(type(selectd_song))
        mixer.music.load(selectd_song)
        mixer.music.play()
        # Getting the length of the file
        song = MP3(filename)
        song_length = int(song.info.length)
        progress_bar['maximum'] = song_length

        def length():
            #Give the current postion of the music
            current_pos = mixer.music.get_pos()//1000
            progress_bar['value'] = current_pos
            progress_bar.after(1, length)
        length()
    except:
        box.showerror("Error", "I think no music  is selectd")


menubar = Menu(window)
menubar.configure(bg="Orange")
menubar.add_command(label="About", command=about)
# Importing all the images
play_img = PhotoImage(file='play.png')
stop_img = PhotoImage(file='stop.png')
pause_img = PhotoImage(file='pause.png')
mute_img = PhotoImage(file='mute.png')
unmute_img = PhotoImage(file='unmute.png')
list_box = Listbox(window, width=25, height=15)
play_btn = Button(window, image=play_img, command=play)
pause_btn = Button(window, image=pause_img, command=pause)
stop_btn = Button(window, image=stop_img, command=stop)
mute_btn = Button(window, image=mute_img, command=mute)
sound_bar = Scale(window, from_=0, to=100, orient=HORIZONTAL, command=voice)
sound_bar.set(50)
add_btn = Button(window, text="Add +", command=add)
progress_bar = Progressbar(window, orient=HORIZONTAL, length=250)
list_box.grid(row=1, column=1, rowspan=2)
play_btn.grid(row=1, column=2, padx=5)
pause_btn.grid(row=1, column=3, padx=5)
stop_btn.grid(row=1, column=4)
mute_btn.grid(row=2, column=2, padx=5)
sound_bar.grid(row=2, column=3, columnspan=2)
add_btn.grid(row=3, column=1, pady=5)
progress_bar.grid(row=3, column=2, columnspan=2, padx=10)
window.configure(menu=menubar)
window.mainloop()
