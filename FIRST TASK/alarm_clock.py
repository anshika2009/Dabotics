from tkinter import *
from PIL import Image
import datetime
import time
from pygame import mixer
import threading
from tkinter import messagebox

root=Tk()
root.title("ALARM CLOCK")
root.geometry("530x330")

alarmtime=StringVar()
mesage=StringVar()

head=Label(root,text="Alarm Clock", font=('comic sans',20))
head.grid(row=0,columnspan=3,pady=10)

mixer.init()

def ala():
    a=alarmtime.get()
    alarmt=a
    currentt=time.strftime("%H:%M")
    while currentt!=alarmt:
        currentt=time.strftime("%H:%M")
    if currentt==alarmt:
        mixer.music.load('tone.mp3')
        mixer.music.play()
        msg=messagebox.showinfo('Info',mesage.get())       #f'{mesage.get()}')
        if msg=='ok':
            mixer.music.stop()
            
            
#main
Clockimg=PhotoImage(file='clock.png')
Clockimg = Clockimg.zoom(25)
Clockimg = Clockimg.subsample(75)

img=Label(root,image=Clockimg)
img.grid(rowspan=4,column=0)

inputtime=Label(root,text="Set Time", font=('comic sans',18))
inputtime.grid(row=1,column=1)

altime=Entry(root,textvariable=alarmtime,font=('comic sans',18),width=6)
altime.grid(row=1,column=2)

msg=Label(root,text="Message", font=('comic sans',18))
msg.grid(row=2,column=1,columnspan=2)

msginput=Entry(root,textvariable=mesage, font=('comic sans',18))
msginput.grid(row=3,column=1,columnspan=2)

submit = Button(root,text="SET",font=('comic sans',18),command=ala)
submit.grid(row=4,column=1,columnspan=2)

root.mainloop()