
#Imports
from pygame import mixer
from tkinter import Tk
from tkinter import Button
from tkinter import Label
from tkinter import filedialog


currentVolume=float(0.5)


#Functions
def playSong():
    fileName= filedialog.askopenfilename(initialdir="C:/",title="Please select a file")
    currentSong=fileName
    songTitle=fileName.split("/")
    songTitle=songTitle[-1]
    print(fileName)
    try:
        mixer.init()
        mixer.music.load(currentSong)
        mixer.music.set_volume(currentVolume)
        mixer.music.play()
        songTitleLabel.config(fg="green",text="Playing "+str(songTitle))
        volumeLabel.config(fg="green",text=str(currentVolume))
    except Exception as e:
        print(e)
        songTitleLabel.config(fg="red",text="Error playing music")




def rV():
    try:
        global currentVolume
        if currentVolume<=0:
            volumeLabel.config(fg="red",text="Muted")
            return
        currentVolume-=float(0.1)
        currentVolume=round(currentVolume,1)
        mixer.music.set_volume(currentVolume)
        volumeLabel.config(fg="green",text=(currentVolume))
    except Exception as e:
        print(e)
        songTitleLabel.config(fg="red",text="You haven't selected a song yet")



def iV():
    try:
        global currentVolume
        if currentVolume>=1:
            volumeLabel.config(fg="green",text="Max")
            return
        currentVolume+=float(0.1)
        currentVolume=round(currentVolume,1)
        mixer.music.set_volume(currentVolume)
        volumeLabel.config(fg="green",text=str(currentVolume))
    except Exception as e:
        print(e)
        songTitleLabel.config(fg="red",text="You haven't selected a song yet")


def pause():
    try:
        mixer.music.pause()
    except Exception as e:
        print(e)
        songTitleLabel.config(fg="red",text="You haven't selected a song yet")



def resume():
    try:
        mixer.music.unpause()
    except Exception as e:
        print(e)
        songTitleLabel.config(fg="red",text="You haven't selected a song yet")



#main screen
master=Tk()
master.title("Music Player")




#labels
Label(master,text="Custom Music Player", font=("Zen Dots",15), fg="red").grid(sticky="N", row=0, padx=12)
Label(master,text="Please select the music you want to play", font=("Calibri",12), fg="blue").grid(sticky="N", row=1)
Label(master,text="Volume", font=("Calibri",12), fg="red").grid(sticky="N", row=4)
songTitleLabel=Label(master,font=("Calibri",12))
songTitleLabel.grid(sticky="N",row=3)
volumeLabel=Label(master,font=("Calibri",12))
volumeLabel.grid(sticky="N",row=5)




#Buttons
Button(master,text="Select Song", font=("Calibri",12), command=playSong).grid(row=2,sticky="N")
Button(master,text="Pause", font=("Calibri",12),command=pause).grid(row=3,sticky="E")
Button(master,text="Resume", font=("Calibri",12),command=resume).grid(row=3,sticky="W")
Button(master,text="-", font=("Calibri",12), width=5,command=rV).grid(row=5,sticky="W")
Button(master,text="+", font=("Calibri",12), width=5,command=iV).grid(row=5,sticky="E")



master.mainloop()
