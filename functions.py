from pygame import mixer
from tkinter import filedialog
import tkinter.messagebox as box
mixer.init()


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
