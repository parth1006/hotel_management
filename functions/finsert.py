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
win.title("Functions")
menuBar = Menu(win)
win.config(menu=menuBar)


#1 booking ID
lbid = tk.Label(win, text="Booking ID : ") 		
lbid.grid(column=0, row=10)

bid = tk.StringVar() 
tbid = tk.Entry(win, width=20, textvariable=bid) 
tbid.grid(column=1, row=10)


#2 Functions type
lftype = tk.Label(win, text="Function Type : ") 		
lftype.grid(column=0, row=12)

ftype = tk.StringVar() 
tftype = tk.Entry(win, width=20, textvariable=ftype) 
tftype.grid(column=1, row=12)

#3 cname
lcname = tk.Label(win, text="Client Name : ") 		
lcname.grid(column=0, row=14)

cname = tk.StringVar() 
tcname= tk.Entry(win, width=20, textvariable=cname) 
tcname.grid(column=1, row=14)

#4 Booking date

lbdate = tk.Label(win, text="Booking date : ") 		
lbdate.grid(column=0, row=16)

bdate = tk.StringVar() 
tbdate = tk.Entry(win, width=20, textvariable=bdate) 
tbdate.grid(column=1, row=16)

# Check in date
lidate= tk.Label(win, width= 20, text="Check in date : ")
lidate.grid(column=0, row=18)

idate= tk.StringVar()
tidate= tk.Entry(win, width= 20, textvariable= idate)
tidate.grid(column= 1, row= 18)

# check out date
lodate = tk.Label(win, text = "Check Out date : ")
lodate. grid(column=0, row= 20)

odate = tk.StringVar()
todate= tk.Entry(win, width=20, textvariable= odate)
todate.grid(column= 1, row=20)


# no of rooms booked
lrbook= tk.Label(win, text = "Rooms Booked : ")
lrbook. grid(column=0, row= 22)

rbook = tk.IntVar()
trbook= tk.Entry(win, width=20, textvariable= rbook)
trbook.grid(column= 1, row=22)

# Halls booked
lhbook= tk.Label(win, text = "Halls Booked : ")
lhbook. grid(column=0, row= 24)

hbook = tk.StringVar()
thbook= tk.Entry(win, width=20, textvariable= hbook)
thbook.grid(column= 1, row=24)

# Price

lprice = tk.Label(win, text="Price : ") 		
lprice.grid(column=0, row=26)

price = tk.IntVar() 
tprice= tk.Entry(win, width=20, textvariable=price) 
tprice.grid(column=1, row=26)

def insert(): 				
    try: 
        conn = mysql.connector.connect(host='localhost',database='hotel_management',user='root',password='root',charset='utf8') 
        cursor = conn.cursor() 
        bid1 = bid.get() 
        ftype1 = ftype.get() 
        cname1 = cname.get() 
        bdate1= bdate.get()
        idate1= idate.get()
        odate1=odate.get()
        rbook1=rbook.get()
        hbook1=hbook.get()
        price1=price.get()
        
        cursor.execute("insert into functions values('"+bid1+"','"+ftype1+"','"+cname1+"','"+bdate1+"','"+idate1+"','"+odate1+"',"+str(rbook1)+",'"+hbook1+"',"+str(price1)+");")
        if(cursor.rowcount>0): 
             mBox.showinfo('Congrats',"DONE!!")
             bid.set('')
             ftype.set('')
             cname.set('')
             bdate.set('')
             idate.set('')
             odate.set('')
             rbook.set('')
             hbook.set('')
             price.set('')
            
        else: 
             mBox.showinfo('Warning!', 'Not Found')
        conn.commit()
    except Error as e : 
        print("Error while connecting to MySQL", e) 
    finally: 
        print("MySQL connection is closed")
        
        
insert=tk.Button(win, font=('arial',20), text="Insert", command=insert)
insert.grid(column=3,row=28)
    
