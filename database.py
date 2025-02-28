from tkinter.messagebox import *

def create_table(conn):
    query="CREATE TABLE IF NOT EXISTS accmaster(accno INTEGER PRIMARY KEY,balance int)"
    cur=conn.cursor()
    cur.execute(query)
    conn.commit()

def create_account_db(conn,accno,balance):
    accno=int(accno)
    balance=int(balance)
    query="INSERT into accmaster values(?,?)"
    cur=conn.cursor()
    cur.execute(query,[accno,balance])
    conn.commit()
    if cur.rowcount>0:
        showinfo("BANK","Account Created Succefully")
    else:
        showwarning("BANK","Failed to Create")
    
def get_account_db(conn,accno):
    accno=int(accno)
    query="Select * from accmaster where accno=? "
    cur=conn.cursor()
    cur.execute(query,[accno])
    account=cur.fetchone()
    if account==None:
        showinfo("Bank","Account Not Found")
    else:
        showinfo("Bank",f"Accno:{account[0]}\nBalance:{account[1]}")

def deposit_db(conn,accno,amt):
    accno=int(accno)
    amt=int(amt)
    query="update accmaster set balance=balance+? where accno=? "
    cur=conn.cursor()
    cur.execute(query,[amt,accno])
    conn.commit()
    if cur.rowcount>0:
        showinfo("BANK","Amount Deposited sccessfully")
    else:
        showwarning("BANK","Account Not Found") 

def withdraw_db(conn,accno,amt):
    accno=int(accno)
    amt=int(amt)
    query1="Select * from accmaster where accno=? "
    cur1=conn.cursor()
    cur1.execute(query1,[accno])
    account=cur1.fetchone()
    if account==None:
        showinfo("Bank","Account Not Found")
    else:
        balance=account[1]
        if balance>=amt:
            query2="update accmaster set balance=balance-? where accno=? "
            cur2=conn.cursor()
            cur2.execute(query2,[amt,accno])
            conn.commit()
            if cur2.rowcount>0:
                showinfo("BANK","Amount withdraw sccessfully")
        else:
            showinfo("Bank","Insufficent Balance")