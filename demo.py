from tkinter import *
from tkinter.messagebox import *
import database
import sqlite3

conn=sqlite3.Connection("test.db")
database.create_table(conn)

def mainWindow():
    clearWindow()
    L1=Label(win,text="Banking System",font="Arial 20 bold")
    L1.pack(pady=10)
    b1=Button(win,text="Open Account",width=20,command=OpenAccountWindow)
    b1.pack(side="top",pady=5,ipady=3)
    b2=Button(win,text="Check Account",width=20,command=CheckAccountWindow)
    b2.pack(side="top",pady=5,ipady=3)
    b3=Button(win,text="Deposit",width=20,command=DepositWindow)
    b3.pack(side="top",pady=5,ipady=3)
    b4=Button(win,text="Withdraw",width=20,command=WithdrawWindow)
    b4.pack(side="top",pady=5,ipady=3)
    b5=Button(win,text="Exit",width=20,command=win.destroy)
    b5.pack(side="top",pady=5,ipady=3)    

def OpenAccountWindow():
    clearWindow()
    L1=Label(win,text="Open New Account",font="arial 20 bold")
    L1.pack(pady=2)
    L2=Label(win,text="Accno")
    L2.pack(pady=2)
    E1=Entry(win,width=20)
    E1.pack(pady=2)
    L3=Label(win,text="Balance")
    L3.pack(pady=2)
    E2=Entry(win,width=20)
    E2.pack(pady=2)
    B1=Button(win,text="Create Account",width=20,command=lambda: database.create_account_db(conn,E1.get(),E2.get()))
    B1.pack(pady=5)
    B2=Button(win,text="Back",width=20,command=mainWindow)
    B2.pack(pady=5)

def CheckAccountWindow():
    clearWindow()
    L1=Label(win,text="Check Account Balance",font="arial 20 bold")
    L1.pack(pady=2)
    L2=Label(win,text="Accno")
    L2.pack(pady=2)
    E1=Entry(win,width=20)
    E1.pack(pady=2)
    B1=Button(win,text="Check",width=20,command=lambda: database.get_account_db(conn,E1.get()))
    B1.pack(pady=5)
    B2=Button(win,text="Back",width=20,command=mainWindow)
    B2.pack(pady=5)

def DepositWindow():
    clearWindow()
    L1=Label(win,text="Deposit Amount",font="arial 20 bold")
    L1.pack(pady=2)
    L2=Label(win,text="Accno")
    L2.pack(pady=2)
    E1=Entry(win,width=20)
    E1.pack(pady=2)
    L3=Label(win,text="Amount")
    L3.pack(pady=2)
    E2=Entry(win,width=20)
    E2.pack(pady=2)
    B1=Button(win,text="Deposit",width=20,command=lambda: database.deposit_db(conn,E1.get(),E2.get()))
    B1.pack(pady=5)
    B2=Button(win,text="Back",width=20,command=mainWindow)
    B2.pack(pady=5)

def WithdrawWindow():
    clearWindow()
    L1=Label(win,text="Withdraw Amount",font="arial 20 bold")
    L1.pack(pady=2)
    L2=Label(win,text="Accno")
    L2.pack(pady=2)
    E1=Entry(win,width=20)
    E1.pack(pady=2)
    L3=Label(win,text="Amount")
    L3.pack(pady=2)
    E2=Entry(win,width=20)
    E2.pack(pady=2)
    B1=Button(win,text="Withdraw",width=20,command=lambda: database.withdraw_db(conn,E1.get(),E2.get()))
    B1.pack(pady=5)
    B2=Button(win,text="Back",width=20,command=mainWindow)
    B2.pack(pady=5)


def clearWindow():
    for item in win.winfo_children():
        item.destroy()

win=Tk()
win.geometry("400x300")
win.title("BANK")
mainWindow()

win.mainloop()