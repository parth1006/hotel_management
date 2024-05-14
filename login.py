import tkinter as tk
import numpy as np
import pandas as pd
from tkinter import ttk
from tkinter import Menu
from tkinter import messagebox as mBox
from tkinter import scrolledtext
from tkinter import *
import mysql.connector
from mysql.connector import Error


#Login Window
win = tk.Tk()
win.title("Login Window")

pic2=PhotoImage(file='marriott2.png')
pic2_label=Label(win, image= pic2)
pic2_label.grid(column=0,row=0,columnspan=700, rowspan=700)

#Id field
log = tk.Label(win, text="Login ID : ",background="white")
log.grid(column=0, row=7)
log.configure(font=("arial",20))

usr = tk.StringVar()
nameEntered = tk.Entry(win, width=20, textvariable=usr)
nameEntered.grid(column=1, row=7)

#Pass field
bLabel = tk.Label(win, text="Password : ",background="white")
bLabel.grid(column=0, row=12)
bLabel.configure(font=("arial",20))

pas = tk.StringVar()
pasentered = tk.Entry(win, width=20, textvariable=pas, show='*')
pasentered.grid(column=1, row=12)


# Adding a Login function
def login():
    
    try:
        conn = mysql.connector.connect(host='localhost',database='hotel_management',user='root',password='root',charset='utf8')
        cursor = conn.cursor()
        cursor.execute("select * from login where user='"+usr.get()+"' and password = '"+pas.get()+"'")
        ls = cursor.fetchall()
        if(len(ls)>0):
            
            mBox.showinfo('Welcome','Hello Admin')
            win.destroy()
            import mainwindow
        
            
        elif(usr.get()=='' or pas.get()==''):
                mBox.showerror("Error","All Field are required")

        else: 
            mBox.showerror('Error','Wrong user id or password')

    except Error as e :
        print("Error while connecting to MySQL", e)
    finally:
        print("MySQL connection is closed")
        

# Adding Login Button
login = tk.Button(win,font=('arial',12), text="Login!", command=login)
login.grid(column=1, row=15)

            
            
             
        
