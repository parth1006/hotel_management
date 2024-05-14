import pandas as pd
import tkinter as tk 
from tkinter import ttk
from tkinter import Menu
from tkinter import scrolledtext
from tkinter import *
from tkinter import messagebox as mBox
import mysql.connector
from mysql.connector import Error

root = tk.Tk()
root.title('Current Guests')
root.configure(bg='black')



#--------Column Name---------------
lname=tk.Label(root,text='Name',font=('arial',15),bg='black',fg='gold').grid(column=0,row=0)
lgid=tk.Label(root,text='Guest Id',font=('arial',15),bg='black',fg='gold').grid(column=1,row=0)
lmob=tk.Label(root,text='Mobile No',font=('arial',15),bg='black',fg='gold').grid(column=2,row=0)
lcard=tk.Label(root,text='Adhaar No',font=('arial',15),bg='black',fg='gold').grid(column=3,row=0)
lrno=tk.Label(root,text="Room No",font=('arial',15),bg='black',fg='gold').grid(column=4,row=0)
locc=tk.Label(root,text='Occupancy',font=('arial',15),bg='black',fg='gold').grid(column=5,row=0)
lbdate=tk.Label(root,text='Booking date',font=('arial',15),bg='black',fg='gold').grid(column=6,row=0)
lidate=tk.Label(root,text='check in date',font=('arial',15),bg='black',fg='gold').grid(column=7,row=0)
lodate=tk.Label(root,text='Check out date',font=('arial',15),bg='black',fg='gold').grid(column=8,row=0)

#----------Table-------------------------------------

try:
    
    conn = mysql.connector.connect(host='localhost',database='hotel_management',user='root',password='root',charset='utf8')
    cursor = conn.cursor()
    cursor.execute("select* from guest_list")
    ls = pd.DataFrame(cursor.fetchall())
  
    for i in range(0, len(ls.index)):
        for j in range(0, len(ls.columns)):
            b = tk.Entry(root)
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
