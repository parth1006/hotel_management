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
win.title("Add New Room")
menuBar = Menu(win)
win.config(menu=menuBar)


#1 roomno
lrno = tk.Label(win, text="Room No. : ") 		
lrno.grid(column=0, row=10)

rno = tk.IntVar() 
trno = tk.Entry(win, width=20, textvariable=rno) 
trno.grid(column=1, row=10)


#2 room type
lrtype = tk.Label(win, text="Room type : ") 		
lrtype.grid(column=0, row=12)

rtype = tk.StringVar() 
trtype = tk.Entry(win, width=20, textvariable=rtype) 
trtype.grid(column=1, row=12)

#3 Floor
lfloor = tk.Label(win, text="Floor : ") 		
lfloor.grid(column=0, row=14)

floor = tk.StringVar() 
tfloor= tk.Entry(win, width=20, textvariable=floor) 
tfloor.grid(column=1, row=14)

#4 No of beds

lbeds = tk.Label(win, text="No.of Beds : ") 		
lbeds.grid(column=0, row=16)

beds = tk.IntVar() 
tbeds = tk.Entry(win, width=20, textvariable=beds) 
tbeds.grid(column=1, row=16)

#5 Price
lprice = tk.Label(win, text="Price : ") 		
lprice.grid(column=0, row=18)

price = tk.IntVar() 
tprice= tk.Entry(win, width=20, textvariable=price) 
tprice.grid(column=1, row=18)

def insert(): 				
    try: 
        conn = mysql.connector.connect(host='localhost',database='hotel_management',user='root',password='root',charset='utf8') 
        cursor = conn.cursor() 
        rno1 = rno.get() 
        rtype1 = rtype.get() 
        floor1 = floor.get() 
        beds1 = beds.get()
        price1= price.get()
        
        cursor.execute("insert into room_list values("+str(rno1)+",'"+rtype1+"','"+floor1+"',"+str(beds1)+","+str(price1)+");")
                       
        if(cursor.rowcount>0): 
             mBox.showinfo('Congrats')
             rno.set('')
             rtype.set('')
             floor.set('')
             beds.set('')
             price.set('')
            
        else: 
             mBox.showinfo('Warning!', 'Not Found')       
    except Error as e : 
        print("Error while connecting to MySQL", e) 
    finally: 
        print("MySQL connection is closed")
        conn.commit()
insert=tk.Button(win,font=('arial',16), text="Insert  Details",command=insert)
insert.grid(column=3,row=21)                                                                                                                                                                                     

       
                       
        
