from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import pymysql
from tkinter import ttk
import tkinter as tk

#Functions
def dashboard():
    login_window.destroy()
    import home


def save_data():
    return registrationnumberEntry.get()

def login_user():

    if registrationnumberEntry.get()=='' or passwordEntry.get()=='':
        messagebox.showerror('Error', 'Please enter Registration number and Password')
    else:
        try:
            con=pymysql.connect(host='localhost',user='root',password='Evo9Jw2474')
            mycursor=con.cursor()
        except:*/
            messagebox.showerror('Error', 'Please check Registration number and Password and try again')
            return

        query='use studentdata'
        mycursor.execute(query)
        query='select * from data where registration_number=%s and password=%s'
        mycursor.execute(query,(registrationnumberEntry.get(),passwordEntry.get()))
        row=mycursor.fetchone()
        if row==None:
            messagebox.showerror('Error', 'Invalid Registration number or Password')
        else:


            dashboard()






def on_enter(event):
    if registrationnumberEntry.get()=='Registration Number':
        registrationnumberEntry.delete(0,END)


def password_enter(event):
    if passwordEntry.get() == 'Password':
        passwordEntry.delete(0, END)

def signup_page():
    login_window.destroy()
    import SignUp

def forget_pass():
    login_window.destroy()
    import Forgot_Password


def hide():
    openeye.config(file='close.png')
    passwordEntry.config(show='\u2022')
    eyeButton.config(command=show)

def show():
    openeye.config(file='open.png')
    passwordEntry.config(show='')
    eyeButton.config(command=hide)






#GUI

global registrationnumberEntry
login_window=Tk()
login_window.resizable(0,0)
login_window.title('Student Login Page')

bgImage=ImageTk.PhotoImage(file='background.png')

bgLabel=Label(login_window,image=bgImage)
bgLabel.pack()

heading=Label(login_window,text='Student Login',font=('Microsoft Yahei UI Bold',23,'bold'),bg='white',fg='#57a1f8')
heading.place(x=590,y=125)

registrationnumberEntry=Entry(login_window,width=25,font=('Microsoft Yahei UI',11),bd=0,fg='black')
registrationnumberEntry.place(x=580,y=200)
registrationnumberEntry.insert(0,'Registration Number')
registrationnumberEntry.bind('<FocusIn>',on_enter)

frame1=Frame(login_window,width=250,height=2,bg='black')
frame1.place(x=580,y=222)

passwordEntry=Entry(login_window,width=25,font=('Microsoft Yahei UI',11),bd=0,fg='black')
passwordEntry.place(x=580,y=260)
passwordEntry.insert(0,'Password')
passwordEntry.bind('<FocusIn>',password_enter)

frame2=Frame(login_window,width=250,height=2,bg='black')
frame2.place(x=580,y=282)


openeye=PhotoImage(file='open.png')
eyeButton=Button(login_window,image=openeye,bd=0,bg='white',activebackground='white',
                 cursor='hand2',command=show)
eyeButton.place(x=800,y=255)



forgetButton=Button(login_window,text='Forgot Password?',bd=0,bg='white',activebackground='white',
                 cursor='hand2',font=('Microsoft Yahei UI',9),fg='#57a1f8',activeforeground='#57a1f8',command=forget_pass)
forgetButton.place(x=715,y=295)


loginButton=Button(login_window,text='Login',font=('Open Sans',16,'bold'),fg='white',
                   bg='#57a1f8',activeforeground='white',activebackground='#57a1f8',
                   cursor='hand2',bd=0,width=19,command=login_user)

loginButton.place(x=578,y=350)


signuplabel=Label(login_window,text="Don't have an account?",font=('Open Sans',9,'bold'),bg='white',fg='black')
signuplabel.place(x=578,y=400)

createaccountButton=Button(login_window,text='Create an account',font=('Open Sans',9,'bold underline'),fg='#57a1f8',
                   bg='white',activeforeground='#57a1f8',activebackground='white',
                   cursor='hand2',bd=0,command=signup_page)
createaccountButton.place(x=727,y=400)





login_window.mainloop()