import pandas as pd
import tkinter as tk 
from tkinter import ttk
from tkinter import Menu
from tkinter import scrolledtext
from tkinter import *
from tkinter import messagebox as mBox
import mysql.connector
from mysql.connector import Error

win = tk.Tk()
win.title('Functions List')
win.configure(bg='black')



#--------Column Name---------------
lbid=tk.Label(win,text='Booking Id',font=('arial',15),bg='black',fg='gold').grid(column=0,row=0)
lftype=tk.Label(win,text='Funtion Type',font=('arial',15),bg='black',fg='gold').grid(column=1,row=0)
lcname=tk.Label(win,text='Client Name',font=('arial',15),bg='black',fg='gold').grid(column=2,row=0)
lbdate=tk.Label(win,text='Booking date',font=('arial',15),bg='black',fg='gold').grid(column=3,row=0)
lidate=tk.Label(win,text='Check In ',font=('arial',15),bg='black',fg='gold').grid(column=4,row=0)
lodate=tk.Label(win,text='Check Out',font=('arial',15),bg='black',fg='gold').grid(column=5,row=0)
lrbook=tk.Label(win,text='Rooms Booked',font=('arial',15),bg='black',fg='gold').grid(column=6,row=0)
lhbook=tk.Label(win,text='Halls Booked',font=('arial',15),bg='black',fg='gold').grid(column=7,row=0)
lprice=tk.Label(win,text='Price',font=('arial',15),bg='black',fg='gold').grid(column=8,row=0)

#----------Table-------------------------------------

try:
    
    conn = mysql.connector.connect(host='localhost',database='hotel_management',user='root',password='root',charset='utf8')
    cursor = conn.cursor()
    cursor.execute("select* from functions")
    ls = pd.DataFrame(cursor.fetchall())
  
    for i in range(0, len(ls.index)):
        for j in range(0, len(ls.columns)):
            b = tk.Entry(win)
            b.insert(0, ls.iloc[i][j])
            b.grid(row=i+1, column=j)
            b.config(state = "readonly")
    conn.commit()        
            
except Error as e :
    print("Error while connecting to MySQL", e)
finally:
    print("MySQL connection is closed")
#------------------------------------------------------    



tk.mainloop()
