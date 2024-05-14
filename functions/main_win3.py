import pandas as pd
import numpy as np
import pandas as pd
import tkinter as tk
from tkinter import Menu
from tkinter import messagebox as mBox 
from tkinter import *
from tkinter import scrolledtext

win = tk.Tk()
win.title("Function Details")
menuBar = Menu(win)
win.config(menu=menuBar)

pic=PhotoImage(file='marriott.png')
pic_label= Label(win, image=pic)
pic_label.grid(column=0,row=0,columnspan=4000,rowspan=4000)

def insert():
    import finsert
    win.quit()

def update():
    import fupdate
    win.quit()

def delete():
    import fdelete
    win.quit()

def table():
    import fpopuptable
    win.quit()

def search():
    import fsearch
    win.quit()
# table

tableMenu = Menu(menuBar, tearoff=0)
menuBar.add_cascade(label="Table", menu=tableMenu)
tableMenu.add_command(label="Show Table",command=table)

#buttons

insert=tk.Button(win,font=('arial',16), text="Insert Details" ,command=insert) 
insert.grid(column=2, row=2,columnspan=1)

update= tk.Button(win, font=('arial',16),text="Update Details", command= update)
update.grid(column=2, row=4, columnspan=1)

delete= tk.Button(win,font= ('arial',16), text= "Delete Details", command= delete)
delete.grid(column=4, row=2, columnspan=1)

search= tk.Button(win,font=('arial',16), text= "Search Details", command= search)
search.grid(column=4,row=4,columnspan=1)

