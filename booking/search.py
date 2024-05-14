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


win= tk.Tk()
win.title("Search Entries")
#1name 
lname = tk.Label(win, text="Guest Name : ") 		
lname.grid(column=0, row=0)



name = tk.StringVar()
tname = tk.Entry(win, width=20, textvariable=name) 
tname.grid(column=1, row=0)

#2guestid 
lgid = tk.Label(win, text="Guest Id : ") 		
lgid.grid(column=0, row=2)

gid = tk.IntVar() 
tgid = tk.Entry(win, width=20, textvariable=gid) 
tgid.grid(column=1, row=2)

#2mobile NO
lmob = tk.Label(win, text="Mobile ") 		
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
lrno = tk.Label(win, text="Room No.: ") 		
lrno.grid(column=0, row=8)

rno = tk.IntVar() 
trno = tk.Entry(win, width=20, textvariable=rno) 
trno.grid(column=1, row=8)

#4occupancy
locc = tk.Label(win, text="Occupancy: ") 		
locc.grid(column=0, row=10)


occ = tk.IntVar() 
tocc = tk.Entry(win, width=20, textvariable=occ) 
tocc.grid(column=1, row=10)

#5 Booking date
lbdate= tk.Label(win,text="Booking date : ")
lbdate.grid(column=0, row=12)

bdate= tk.StringVar()
tbdate= tk.Entry(win, width=20, textvariable= bdate)
tbdate.grid(column=1, row= 12)

# Check in date
lidate= tk.Label(win, width= 20, text="Check in date : ")
lidate.grid(column=0, row=14)

idate= tk.StringVar()
tidate= tk.Entry(win, width= 20, textvariable= idate)
tidate.grid(column= 1, row= 14)
# check out date
lodate = tk.Label(win, text = "Check Out date : ")
lodate. grid(column=0, row= 16)

odate = tk.StringVar()
todate= tk.Entry(win, width=20, textvariable= odate)
todate.grid(column= 1, row=16)

def search():
    try:
        conn = mysql.connector.connect(host='localhost',database='hotel_management',user='root',password='root',charset='utf8')
        cursor = conn.cursor()
        cursor.execute("select*from  Guest_list where Guest_ID= "+str(gid.get()))
        ls=pd.DataFrame(cursor.fetchall())
        if(len(ls.index>0)):
           name.set(ls.iloc[0][0])
           gid.set(ls.iloc[0][1])
           mob.set(ls.iloc[0][2])
           card.set(ls.iloc[0][3])
           occ.set(ls.iloc[0][5])
           rno.set(ls.iloc[0][4])
           bdate.set(ls.iloc[0][6])
           idate.set(ls.iloc[0][7])
           odate.set(ls.iloc[0][8])
        else:
            mBox.showinfo('Error')
        conn.commit()
    except Error as e :
        print("Error while connecting to MySQL", e)
    finally:
        print("MySQL connection is closed")

#button
search= tk.Button(win, font=('arial',16), text='Search', command= search)
search.grid(column=3, row= 18)
