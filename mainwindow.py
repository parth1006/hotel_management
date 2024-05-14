import pandas as pd
import numpy as np
import pandas as pd
import tkinter as tk
from tkinter import Menu
from tkinter import messagebox as mBox 
from tkinter import *
from tkinter import scrolledtext


win = tk.Tk()
win.title("Welcome")
menuBar = Menu(win) 
win.config(menu=menuBar)

pic=PhotoImage(file='marriott4.png')
pic_label= Label(win, image=pic)
pic_label.grid(column=0,row=0,columnspan=4000,rowspan=4000)

def bdetails():
    import main_win
    win.quit()

def rdetails():
    import main_win2
    win.quit()
def fdetails():
    import main_win3
    win.quit()

Booking=tk.Button(win,font=('arial',16), text="Booking" ,command=bdetails) 
Booking.grid(column=100, row=100)

Room = tk.Button(win, font=('arial',16),text="Rooms", command= rdetails)
Room.grid(column=120, row=120)

Functions= tk.Button(win, font=('arial',16), text="Functions", command= fdetails)
Functions.grid(column=140,row=140)
