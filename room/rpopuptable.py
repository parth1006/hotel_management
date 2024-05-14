import pandas as pd
import tkinter as tk 
from tkinter import ttk
from tkinter import Menu
from tkinter import scrolledtext
from tkinter import *
from tkinter import messagebox as mBox
import mysql.connector
from mysql.connector import Error


win=tk.Tk()
win.title('Room list')
win.config(bg='black')


#---------------------Columns Name-------------------------------
lrno=tk.Label(win,text='Room No',font=('arial',15),bg='black',fg='gold').grid(column=0,row=0)
lrtype=tk.Label(win,text='Room type',font=('arial',15),bg='black',fg='gold').grid(column=1,row=0)
lfloor=tk.Label(win,text='Floor',font=('arial',15),bg='black',fg='gold').grid(column=2,row=0)
lbeds=tk.Label(win,text='No of beds',font=('arial',15),bg='black',fg='gold').grid(column=3,row=0)
lprice=tk.Label(win,text='Price',font=('arial',15),bg='black',fg='gold').grid(column=4,row=0)


#----------------table---------------------------------
try:
    
    conn = mysql.connector.connect(host='localhost',database='hotel_management',user='root',password='root',charset='utf8')
    cursor = conn.cursor()
    cursor.execute("select * from Room_list")
    ls = pd.DataFrame(cursor.fetchall())
  
    for i in range(1, len(ls.index)):
        for j in range(0, len(ls.columns)):
            b = tk.Entry(win)
            b.grid(row=i, column=j)
            b.insert(0, ls.iloc[i][j])
            b.config(state = "readonly")
            
           

            
    conn.commit()        
            
except Error as e :
    print("Error while connecting to MySQL", e)
finally:
    print("MySQL connection is closed")
