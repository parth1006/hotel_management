import mysql.connector 
from mysql.connector import Error
import numpy as np
import pandas as pd
import tkinter as tk
from tkinter import Menu
from tkinter import messagebox as mBox 
from tkinter import *


win = tk.Tk()
win.title("Delete Room")
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

def search():
    try:
        conn = mysql.connector.connect(host='localhost',database='hotel_management',user='root',password='root',charset='utf8')
        cursor = conn.cursor()
        cursor.execute("select * from  Room_list where Room_no= "+str(rno.get()))
        ls=pd.DataFrame(cursor.fetchall())
        if(len(ls.index)>0):
           rno.set(ls.iloc[0][0])
           rtype.set(ls.iloc[0][1])
           floor.set(ls.iloc[0][2])
           beds.set(ls.iloc[0][3])        
           price.set(ls.iloc[0][4])
        else: 
             mBox.showinfo('Not Found')       
    except Error as e : 
        print("Error while connecting to MySQL", e) 
    finally: 
        print("MySQL connection is closed")


def delete():
    try:
        conn = mysql.connector.connect(host='localhost',database='hotel_management',user='root',password='root',charset='utf8')
        cursor = conn.cursor()
        cursor.execute("delete from room_list where room_no="+str(rno.get()))
        if(cursor.rowcount>0):
         mBox.showinfo('Deleted')
         rno.set('')
         rtype.set('')
         floor.set('')
         beds.set('')
         price.set('')
        else:
            mBox.showinfo('Error')
        conn.commit()
    except Error as e:
        print ("Error whitle connecting to MySQL",e)
    finally:
        print("MySQL connection is closed")

delete = tk.Button(win,font=('arial',12), text = "Delete", command= delete)
delete.grid(column=3, row=24)

search = tk.Button(win,font=('arial',12), text ="Search",command = search)
search.grid(column=3, row= 20)
