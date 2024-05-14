import mysql.connector 
from mysql.connector import Error
import pandas as pd
import numpy as np
import pandas as pd
import tkinter as tk
from tkinter import Menu
from tkinter import messagebox as mBox 
from tkinter import *
from tkinter import scrolledtext


win = tk.Tk()
win.title("Insert details")

menuBar = Menu(win)
win.config(menu=menuBar)

#1name 
lname = tk.Label(win, text="Guest Name") 		
lname.grid(column=0, row=0)



name = tk.StringVar()
tname = tk.Entry(win, width=20, textvariable=name) 
tname.grid(column=1, row=0)

#2guestid 
lgid = tk.Label(win, text="Guest Id") 		
lgid.grid(column=0, row=2)

gid = tk.IntVar() 
tgid = tk.Entry(win, width=20, textvariable=gid) 
tgid.grid(column=1, row=2)

#2mobile NO
lmob = tk.Label(win, text="Mobile") 		
lmob.grid(column=0, row=4)

mob = tk.IntVar() 
tmob = tk.Entry(win, width=20, textvariable=mob) 
tmob.grid(column=1, row=4)

# adhhar card
lcard = tk.Label(win, text="Adhaar Card ") 		
lcard.grid(column=0, row=6)

card = tk.IntVar() 
tcard = tk.Entry(win, width=20, textvariable=card) 
tcard.grid(column=1, row=6)
#3roomno
lrno = tk.Label(win, text="Room No.") 		
lrno.grid(column=0, row=8)

rno = tk.IntVar() 
trno = tk.Entry(win, width=20, textvariable=rno) 
trno.grid(column=1, row=8)

#4occupancy
locc = tk.Label(win, text="Occupancy") 		
locc.grid(column=0, row=10)

occ = tk.IntVar() 
tocc = tk.Entry(win, width=20, textvariable=occ) 
tocc.grid(column=1, row=10)

#5 Booking date
lbdate= tk.Label(win,text="Booking date")
lbdate.grid(column=0, row=12)

bdate= tk.StringVar()
tbdate= tk.Entry(win, width=20, textvariable= bdate)
tbdate.grid(column=1, row= 12)

# Check in date
lidate= tk.Label(win, width= 20, text="Check in date")
lidate.grid(column=0, row=14)

idate= tk.StringVar()
tidate= tk.Entry(win, width= 20, textvariable= idate)
tidate.grid(column= 1, row= 14)
# check out date
lodate = tk.Label(win, text = "Check Out date")
lodate. grid(column=0, row= 16)

odate = tk.StringVar()
todate= tk.Entry(win, width=20, textvariable= odate)
todate.grid(column= 1, row=16)


#insert
def insert(): 				
    try: 
        conn = mysql.connector.connect(host='localhost',database='hotel_management',user='root',password='root',charset='utf8') 
        cursor = conn.cursor() 
        name1 = name.get() 
        gid1 = gid.get()
        mob1= mob.get()
        card1=card.get()
        rno1 = rno.get() 
        occ1 = occ.get()
        bdate1= bdate.get()
        idate1= idate.get()
        odate1=odate.get()
        
        cursor.execute("insert into guest_list values('"+name1+"',"+str(gid1)+","+str(mob1)+","+str(card1)+","+str(rno1)+","+str(occ1)+",'"+bdate1 +"','"+idate1+"','"+odate1+"');")
                            

       
                       
                       
        if(cursor.rowcount>0): 
             mBox.showinfo('Congrats','Done!')
             name.set('')
             gid.set('')
             mob.set('')
             card.set('')
             rno.set('')
             occ.set('')
             bdate.set('')
             idate.set('')
             odate.set('')
            
        else: 
             mBox.showinfo('Warning!', 'Not Found')       
    except Error as e : 
        print("Error while connecting to MySQL", e) 
    finally: 
        print("MySQL connection is closed")
        conn.commit()
insert= tk.Button(win,font=('arial',16),text="Insert",command= insert)
insert.grid(column=3,row=18)
