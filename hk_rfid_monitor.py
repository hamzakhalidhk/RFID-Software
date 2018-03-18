import serial
from tkinter import messagebox
import ttk
import sqlite3
import time
import datetime
try:
    from tkinter import *
except:
    from tkinter import *


def pro():
    messagebox.showinfo(title= "About Project", message="RFID attendance system made by Fabiha Umar. ")
    return
def dev():
    messagebox.showinfo(title= "About Developer", message="This is a python based software made by HK developers. Place an order at: itshamzakhalidhk@gmail.com")
    return
def ex():
    ex = messagebox.askyesno(title= "Quit", message="Are you Sure?")
    if ex >0:
        root.destroy()
        return
thing = ' '

class main:

    db_name = 'rfid.db'
    def __init__(self,root,ser):
        self.ser=ser
        self.root=root
        self.root.title("RFID DATA MONITOR")
        self.root.geometry('700x300-30+30')
        self.root.resizable(width=False,height=False)

        self.s = StringVar()
        self.s1 = StringVar()
        self.s2 = StringVar()

        self.tree = ttk.Treeview(root)
        self.tree["columns"] = ("TimeStamp", "ID", "UserName", "RollNo")
        self.tree.column("TimeStamp", width=150)
        self.tree.column("ID", width=100)
        self.tree.column("UserName", width=100)
        self.tree.column("RollNo", width=100)
        self.tree.heading("TimeStamp", text="Time")
        self.tree.heading("ID", text="ID")
        self.tree.heading("UserName", text="Name")
        self.tree.heading("RollNo", text="Roll Number")
        self.tree.pack()
        self.root.after(60,self.min)

    def min(self):

        thing = self.ser.readline().decode('ascii')
        string = str(thing)
        print(string)
        i=0
        j=0
        k=0
        for i in range(2, len(string)):
            if string[i] == ';':
                break
        v = string[3:i]
        for j in range(10, len(string)):
            if string[j] == ';':
                break
        c = string[i + 7:j]
        for k in range(20, len(string)):
            if string[k] == len(string):
                break
        p = string[j + 13:k-1]
        self.s.set(v)
        self.s1.set(c)
        self.s2.set(p)
        self.root.after(500, self.min)

        conn = sqlite3.connect('rfid.db')
        call = conn.cursor()
        if len(v)>0 and len(c)>0 and len(p)>0:
            print("id= " + v)
            print("i= " + c)
            print("p= " + p)
            unix = time.time()
            date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
            call.execute("INSERT INTO rfid (datestamp, id, name, rollnumber) VALUES (?,?,?,?)", (date, v, c, p))
            conn.commit()

            call.execute('SELECT * FROM rfid ORDER BY datestamp DESC LIMIT 5')
            for row in call.fetchall():
                    print(row)
            self.tree.insert("", 0, text="FETCHED --- >", values=(date, v, c, p))
        self.root.update()
        # Hamza Khalid Data ---> Voltage: 128V Current: 128A Load: 128W

def stopServer():
    sure=messagebox.askyesno(title='Quit',message='Are you Sure?')
    if sure >0:
        root.destroy()
        return
def startServer():
    try:
        com = portNo.get()
        ser = serial.Serial(com, 9600, timeout=0)
        print('Serial port is open')
        main(root,ser)
        Button1.destroy()
        Button2 = Button(root, text='       Stop Server and Exit      ', command=stopServer, font=("Arial","14"))
        Button2.place(x=230, y=240)
    except:
        Labelerror = Label(root, text='Invalid Port or Error Reading', font=("Arial","14"),  fg='red')
        Labelerror.place(x=110, y=150)
    return

root = Tk()

portNo = StringVar()
root.geometry("500x250+50+50")
root.title('RFID DATA MONITOR')
root.resizable(width=False,height=False)
Labelh=Label(root,text='Enter port Name. E.g: COM4',font=("Arial","14")).place(x=120,y=40)
entry1=Entry(root,textvariable=portNo).place(x=185,y=80)
Button1= Button(root,text='Start Server', command=startServer, font=("Arial","10") )
Button1.place(x=205,y=110)

#Menu
menubar=Menu(root)
optionsmenu = Menu(menubar, tearoff = 0)
optionsmenu.add_command(label="Project", command = pro)
optionsmenu.add_command(label="Developer", command = dev )
optionsmenu.add_command(label="Exit", command= ex)
optionsmenu.add_separator()
menubar.add_cascade(label="Options",menu=optionsmenu)
root.config(menu=menubar)
root.mainloop()
