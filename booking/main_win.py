import pandas as pd
import numpy as np
import pandas as pd
import tkinter as tk
from tkinter import Menu
from tkinter import messagebox as mBox 
from tkinter import *
from tkinter import scrolledtext


win = tk.Tk()

win.title("Guest details")


menuBar = Menu(win) 
win.config(menu=menuBar)

'''pic=PhotoImage(file='marriott.png')
pic_label= Label(win, image=pic)
pic_label.grid(column=0,row=0,columnspan=4000,rowspan=4000)'''

def insrt(): 				
    import insert
    win.quit()

def delte ():
    import delete
    win.quit()

def Table():
    import popuptable
    win.quit()

def udate():
    import update
    win.quit()
def search():
    import search
    win.quit()
    
#table
tableMenu = Menu(menuBar, tearoff=0)
menuBar.add_cascade(label="Table", menu=tableMenu)
tableMenu.add_command(label="Show Table",command=Table)



#button

insertt=tk.Button(win,font=('arial',16), text="Insert Details" ,command=insrt) 
insertt.grid(column=2, row=2,columnspan=1)

update = tk.Button(win, font=('arial',16),text="Update Details", command= udate)
update.grid(column=2, row=4, columnspan=1)

delete= tk.Button(win,font= ('arial',16), text= "Delete Details", command= delte)
delete.grid(column=4, row=2, columnspan=1)

search= tk.Button(win, font=('arial',16),text= "Search Details", command= search)
search.grid(column= 4, row=4, columnspan=1)





