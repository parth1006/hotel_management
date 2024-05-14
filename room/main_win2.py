import pandas as pd
import numpy as np
import pandas as pd
import tkinter as tk
from tkinter import Menu
from tkinter import messagebox as mBox 
from tkinter import *
from tkinter import scrolledtext


win = tk.Tk()
win.title("Room Deatils")
menuBar = Menu(win)
win.config(menu=menuBar)


pic=PhotoImage(file='marriott3.png')
piclabel= Label(win,image=pic)
piclabel.grid(column=0,row=0,columnspan=4000,rowspan=4000)

def table():
    import rpopuptable
    win.quit()

def insert():
    import rinsert
    win.quit()

def delete():
    import rdelete
    win.quit()

def update():
    import rupdate
    win.quit()

def search():
    import rsearch
    win.quit()
tableMenu = Menu(menuBar, tearoff=0)
menuBar.add_cascade(label="Room Table", menu=tableMenu)
tableMenu.add_command(label="Show Table",command=table)


insert= tk.Button(win,font=('arial',16), text="Insert  Details",command=insert)
insert.grid(column=0,row=2)

update=tk.Button(win,font=('arial',16), text="Update Details",command=update)
update.grid(column=0,row=4)

delete=tk.Button(win,font=('arial',16), text="Delete  Details",command=delete)
delete.grid(column=2,row=2)

search=tk.Button(win,font=('arial',16), text="Search Details", command= search)
search.grid(column=2,row=4)
