from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import webbrowser
from tkinter import Tk, Label
import tkinter as tk
from tkinter import messagebox
import pymysql

def logout():
    module_window.destroy()
    import signin


def clear():
    modulecodeEntry.delete(0, END)
    modulenameEntry.delete(0, END)
    creditEntry.delete(0, END)
    gpaEntry.delete(0, END)

def connection():
    con = pymysql.connect(host='localhost', user='root', password='1234')
    return con

def on_home_button_click():
    webbrowser.open('https://www.university.com/')

def logout():
    module_window.destroy()
    import signin

def change_settingsmod():
    module_window.destroy()
    import changesettings

def home_click():
    module_window.destroy()
    import home

def reverse(tuples):
    new_tup=tuples[::-1]
    return new_tup


def moduledatabase():
    modulecode = str(modulecodeEntry.get())
    modulename = str(modulenameEntry.get())
    modulecredit = str(creditEntry.get())
    modulegpa = str(gpaEntry.get())

    if modulecode == "" or modulename == "" or modulecredit == "" or modulegpa == "":
        messagebox.showerror('Error', 'Please fill in all the details')
    else:
        try:
            con = pymysql.connect(host='localhost', user='root', password='1234')
            mycursor = con.cursor()
        except:
            messagebox.showerror('Error', 'Your data was unable to record. Please try again')
            return

        try:
            query = 'use studentdata'
            mycursor.execute(query)
            query = 'create table modules(id int auto_increment primary key not null,registration_number varchar(20),module_code varchar(10),module_name varchar(100),module_credit varchar(10),gpa_ngpa varchar(10))'
            mycursor.execute(query)
        except:
            mycursor.execute('use studentdata')

        reg_no = registrationnumberEntry.get()

        query = 'select * from modules where module_code=%s'
        mycursor.execute(query, (modulecode,))

        row = mycursor.fetchone()
        if row is not None:
            messagebox.showerror('Error', 'You have already enrolled in this Module')
        else:
            query = 'insert into modules(registration_number,module_code,module_name,module_credit,gpa_ngpa) values(%s,%s,%s,%s,%s)'
            mycursor.execute(query, (reg_no, modulecode, modulename, modulecredit, modulegpa))
            con.commit()
            con.close()
            messagebox.showinfo('Success', 'You have successfully enrolled in this Module')
            refreshTable()

def refreshTable():

    my_tree.delete(*my_tree.get_children())


    data = read()


    for row in data:
        my_tree.insert("", "end", values=row[2:])


    my_tree.tag_configure('orow', background="#EEEEEE", font=('Arial', 12))
    num_entries = len(data)
    my_tree_height = 10*24
    other_widgets_height = 150
    my_tree.place(x=160, y=other_widgets_height, height=my_tree_height)


def update():
    selectedmodulecode = ""
    try:
        selected_item = my_tree.selection()[0]
        selectedmodulecode = str(my_tree.item(selected_item)['values'][0])

    except IndexError:
        messagebox.showinfo("Error", "Please select a data row")
        return

    modulecode = str(modulecodeEntry.get())
    modulename = str(modulenameEntry.get())
    modulecredit = str(creditEntry.get())
    modulegpa = str(gpaEntry.get())

    if (modulecode == "" or modulecode.isspace()) or (modulename == "" or modulename.isspace()) or (modulecredit == "" or modulecredit.isspace()) or (modulegpa == "" or modulegpa.isspace()):
        messagebox.showinfo("Error", "Please fill up the blank entry")
        return
    else:
        try:
            con = pymysql.connect(host='localhost', user='root', password='1234')

            cursor = con.cursor()
            cursor.execute('USE studentdata')
            cursor.execute("UPDATE modules SET module_code='" +
                           modulecode + "',module_name='" +
                           modulename + "',module_credit='" +
                           modulecredit + "',gpa_ngpa='" +
                           modulegpa +  "' WHERE module_code='" +
                           selectedmodulecode + "' ")
            con.commit()
            con.close()
        except Exception as e:
            messagebox.showinfo("Error", f"Error updating data: {e}")
            return

    refreshTable()

def setph(word,num):
    if num==1:
        ph1.set(word)
    if num == 2:
        ph2.set(word)
    if num == 3:
        ph3.set(word)
    if num == 4:
        ph4.set(word)


def read():
    reg_no = registrationnumberEntry.get()
    con = pymysql.connect(host='localhost', user='root', password='1234', database='studentdata')
    cursor = con.cursor()
    cursor.execute("SELECT * FROM modules WHERE registration_number=%s", (reg_no,))
    results = cursor.fetchall()
    con.commit()
    con.close()
    return results


def add():
    modulecode=str(modulecodeEntry.get())
    modulename=str(modulenameEntry.get())
    modulecredit=str(creditEntry.get())
    modulegpa=str(gpaEntry.get())

    if(modulecode=="" or modulename=="" or modulecredit=="" or modulegpa==""):
        messagebox.showerror('Error', 'Please fill the all details')

    else:
        try:
            con = connection()
            cursor = con.cursor()
            cursor.execute(
                "INSERT INTO modules VALUES('" + modulecode+ "','" + modulename + "','" + modulecredit + "','" + modulegpa + "')")
            con.commit()
            con.close()
        except:
            messagebox.showerror('Error', 'Module Code Exists')
            return
        refreshTable()

def delete():
    decision = messagebox.askquestion("Warning!!", "Are you sure that you want to unEnrol?")
    if decision != "yes":
        return
    else:
        try:
            selected_item = my_tree.selection()[0]
            modulecode = str(my_tree.item(selected_item)['values'][0])
            modulename = str(my_tree.item(selected_item)['values'][1])
            modulecredit = str(my_tree.item(selected_item)['values'][2])
            modulegpa = str(my_tree.item(selected_item)['values'][3])

            con = pymysql.connect(host='localhost', user='root', password='1234', database='studentdata')
            mycursor = con.cursor()

            query = 'select * from modules where module_code=%s'
            mycursor.execute(query, (modulecode,))
            row = mycursor.fetchone()


            query = "DELETE FROM modules WHERE module_code=%s"
            mycursor.execute(query, (modulecode,))
            con.commit()
            con.close()


            refreshTable()

        except Exception as e:
            print("Error deleting:", e)
            messagebox.showinfo("Error", 'Sorry, an error occurred while deleting the data')



def select():
    try:
        selected_item = my_tree.selection()[0]
        moduleid = str(my_tree.item(selected_item)['values'][0])
        modulename = str(my_tree.item(selected_item)['values'][1])
        modulecredit = str(my_tree.item(selected_item)['values'][2])
        modulegpa = str(my_tree.item(selected_item)['values'][3])


        setph(moduleid, 1)
        setph(modulename, 2)
        setph(modulecredit, 3)
        setph(modulegpa, 4)


    except:
        messagebox.showinfo("Error", "Please select a data row")









module_window = Tk()



module_window.resizable(0, 0)
module_window.title('Module Enrolment Page')


bgImage = ImageTk.PhotoImage(file='homec.png')
bgLabel = Label(module_window, image=bgImage)
bgLabel.grid(row=0, column=0, sticky='nsew')

heading = Label(module_window, text='Module Enrolment', font=('Microsoft Yahei UI bold', 22, 'bold'), bd=0,
                fg='black', bg='white')
heading.place(x=410,y=110)

frame = Frame(module_window, bg='white')
frame.place(x=158,y=400)

modulecodeLabel = Label(frame, text='Module Code', font=('Microsoft Yahei UI', 10, 'bold'), bg='white', fg='#57a1f8')
modulecodeLabel.grid(row=0, column=0, sticky='w', padx=10, pady=10)

ph1=tk.StringVar()
modulecodeEntry = Entry(frame, width=45, font=('Microsoft Yahei UI', 10), fg='black',textvariable=ph1)
modulecodeEntry.grid(row=0, column=1, sticky='w')

ph2=tk.StringVar()


modulename1Label=Label(frame,text='Module Name',font=('Microsoft Yahei UI',10,'bold'),bg='white',fg='#57a1f8')
modulename1Label.grid(row=1,column=0,sticky='w',padx=10,pady=10)

modulenameEntry=Entry(frame,width=45,font=('Microsoft Yahei UI',10),fg='black',textvariable=ph2)
modulenameEntry.grid(row=1,column=1,sticky='w')



ph3=tk.StringVar()
creditLabel=Label(frame,text='Credit',font=('Microsoft Yahei UI',10,'bold'),bg='white',fg='#57a1f8')
creditLabel.grid(row=2,column=0,sticky='w',padx=10,pady=10)

creditEntry=Entry(frame,width=45,font=('Microsoft Yahei UI',10),fg='black',textvariable=ph3)
creditEntry.grid(row=2,column=1,sticky='w')



ph4=tk.StringVar()
gpaLabel=Label(frame,text='GPA/NGPA',font=('Microsoft Yahei UI',10,'bold'),bg='white',fg='#57a1f8')
gpaLabel.grid(row=3,column=0,sticky='w',padx=10,pady=10)

gpaOptions = ["GPA", "NGPA"]

gpaEntry = ttk.Combobox(frame, values=gpaOptions, width=43, font=('Microsoft Yahei UI', 10), state="readonly",textvariable=ph4)
gpaEntry.grid(row=3, column=1, sticky='w')


gpaEntry.set("GPA")


style = ttk.Style()
style.configure("Treeview.Heading", font=('Arial bold', 15))

my_tree = ttk.Treeview(module_window)
my_tree['columns'] = ("Module Code", "Module Name", "Credit", "GPA/NGPA")
my_tree.column("#0", width=0, stretch=NO)
my_tree.column("Module Code", anchor=W, width=150)
my_tree.column("Module Name", anchor=W, width=350)
my_tree.column("Credit", anchor=W, width=100)
my_tree.column("GPA/NGPA", anchor=W, width=150)

my_tree.heading("Module Code", text="Module Code", anchor=W)
my_tree.heading("Module Name", text="Module Name", anchor=W)
my_tree.heading("Credit", text="Credit", anchor=W)
my_tree.heading("GPA/NGPA", text="GPA/NGPA", anchor=W)

my_tree.tag_configure(module_window, background="#EEEEEE", font=('Arial Bold', 15))
my_tree.place(x=160,y=160)

enterButton=Button(module_window,text='Enrol',width=10,bd=0, highlightthickness=0,font=('Microsoft Yahei UI',12,'bold'),bg='#1697d1',activebackground='#1697d1',
                 cursor='hand2',fg='white',activeforeground='white',command=moduledatabase)
enterButton.place(x=703,y=410)

updateButton=Button(module_window,text='Edit',width=10,bd=0, highlightthickness=0,font=('Microsoft Yahei UI',12,'bold'),bg='#1697d1',activebackground='#1697d1',
                 cursor='hand2',fg='white',activeforeground='white',command=update)
updateButton.place(x=703,y=458)

deleteButton=Button(module_window,text='UnEnrol',width=10,bd=0, highlightthickness=0,font=('Microsoft Yahei UI',12,'bold'),bg='#1697d1',activebackground='#1697d1',
                 cursor='hand2',fg='white',activeforeground='white',command=delete)
deleteButton.place(x=703,y=503)

select_Button=Button(module_window,text='Select',width=10,bd=0, highlightthickness=0,font=('Microsoft Yahei UI',12,'bold'),bg='#1697d1',activebackground='#1697d1',
                 cursor='hand2',fg='white',activeforeground='white',command=select)
select_Button.place(x=705,y=548)



home = PhotoImage(file='test1.png')
homeButton = Button(module_window, image=home, bd=0, highlightthickness=0, activebackground='#1697d1',
                    cursor='hand2',command=home_click)
homeButton.place(x=28, y=120)

enrol = PhotoImage(file='enrol.png')
enrolButton = Button(module_window, image=enrol, bd=0, highlightthickness=0, activebackground='#1697d1',
                     cursor='hand2')
enrolButton.place(x=19, y=260)

web = PhotoImage(file='web.png')
webButton = Button(module_window, image=web, bd=0, highlightthickness=0, activebackground='#1697d1',
                   cursor='hand2', command=on_home_button_click)
webButton.place(x=30, y=394)

settings = PhotoImage(file='settings.png')
settingsButton = Button(module_window, image=settings, bd=0, highlightthickness=0, activebackground='#1697d1',
                        cursor='hand2',command=change_settingsmod)
settingsButton.place(x=28, y=526)


registrationnumberLabel = Label(module_window, text='Your Registration Number : ', font=('Microsoft Yahei UI bold', 10, 'bold'), bg='#ecf5fb',
                             fg='#57a1f8')
registrationnumberLabel.place(x=580, y=50)

registrationnumberEntry = Entry(module_window, width=12, font=('Microsoft Yahei UI bold', 10), fg='black')
registrationnumberEntry.place(x=780, y=50)

registrationnumberEntry.insert(0, 'EG/')

LogoutButton=Button(module_window,text='Logout',font=('Open Sans bold',11,'bold'),fg='black',
                   bg='firebrick1',activeforeground='black',activebackground='firebrick1',
                   cursor='hand2',bd=0,command=logout)
LogoutButton.place(x=870,y=562)


module_window.mainloop()



