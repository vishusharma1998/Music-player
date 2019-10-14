from tkinter import *
from pygame import mixer
##import matplotlib
root = Tk()

mixer.init() #initializing the mixer

root.geometry('300x300')
root.title("Melody")
root.iconbitmap(r'F:\\tk project\\play_n8f_icon.ico')

text = Label(root,text ='Lets some play music')
text.pack()


def play_music():
    mixer.music.load("F:\\tk project\\kinna_sona.mp3")
    mixer.music.play()
    print("Hey! This is play button ")

playPhoto = PhotoImage(file='F:\\tk project\\002-play-button.png')
playBtn = Button(root, image = playPhoto, command = play_music)
playBtn.pack()

root.mainloop()



