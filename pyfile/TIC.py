import tkinter.messagebox
from tkinter import messagebox
from tkinter import *
play = Tk()
play.geometry("600x500")
play.title("TIC-TAK-TOE")
play.configure(bg="LightBlue")
PlayerA = StringVar()
PlayerB = StringVar()
P1 = StringVar()
P2 = StringVar()
button = StringVar()
bclink = True
turns = 0
def btnclick(buttons):
    global PlayerA,PlayerB,turns,bclick
    if buttons["text"]=="" and bclick==True:
        buttons["text"]="x"
        bclick=False


play.mainloop()