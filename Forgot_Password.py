from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import pymysql

#function

def hide():
    openeye.config(file='close.png')
    passwordEntry.config(show='\u2022')
    eyeButton.config(command=show)

def show():
    openeye.config(file='open.png')
    passwordEntry.config(show='')
    eyeButton.config(command=hide)

def hide1():
    openeye1.config(file='close.png')
    confirmpasswordEntry.config(show='\u2022')
    eyeButton1.config(command=show1)

def show1():
    openeye1.config(file='open.png')
    confirmpasswordEntry.config(show='')
    eyeButton1.config(command=hide1)

def back():
    forgot_password_window.destroy()
    import signin

def change_password():
    if confirmpasswordEntry.get()=='' or  passwordEntry.get()=='' or registrationnumEntry.get()=='' or contactnumberEntry.get()=='':
        messagebox.showerror('Error','Please fill the all details')

    elif confirmpasswordEntry.get()!=passwordEntry.get():
        messagebox.showerror('Error','Passwords do not match. Please double-check and try again')

    else:
        con = pymysql.connect(host='localhost', user='root', password='Evo9Jw2474',database='studentdata')
        mycursor = con.cursor()
        query = 'select * from data where registration_number=%s and contact_number=%s'
        mycursor.execute(query, (registrationnumEntry.get(), contactnumberEntry.get()))
        row = mycursor.fetchone()

        if row == None:
            messagebox.showerror('Error', 'Invalid Registration number or Contact Number')
        else:
            query = 'update data set password=%s where registration_number=%s'
            mycursor.execute(query, (passwordEntry.get(), registrationnumEntry.get()))
            con.commit()
            con.close()
            messagebox.showinfo('Success', 'Password has been Changed')
            forgot_password_window.destroy()
            import signin












#UI
forgot_password_window=Tk()
forgot_password_window.resizable(0,0)
forgot_password_window.title('Change Password')

bgImage1=ImageTk.PhotoImage(file='background.png')

bgLabel1=Label(forgot_password_window,image=bgImage1)
bgLabel1.pack()

heading=Label(forgot_password_window,text='Change the Password',font=('Microsoft Yahei UI Bold',18,'bold'),bg='white',fg='black')
heading.place(x=568,y=115)


registration=Label(forgot_password_window,text='Registration Number',font=('Microsoft Yahei UI',11,'bold'),bd=0,fg='#57a1f8',bg='white')
registration.place(x=580,y=175)

registrationnumEntry=Entry(forgot_password_window,width=25,font=('Microsoft Yahei UI',11),bd=0,fg='black')
registrationnumEntry.place(x=580,y=205)
registrationnumEntry.insert(0,'')

frame1=Frame(forgot_password_window,width=250,height=2,bg='#57a1f8')
frame1.place(x=580,y=227)




contactnumber=Label(forgot_password_window,text='Your Contact Number',font=('Microsoft Yahei UI',11,'bold'),bd=0,fg='#57a1f8',bg='white')
contactnumber.place(x=580,y=250)

contactnumberEntry=Entry(forgot_password_window,width=25,font=('Microsoft Yahei UI',11),bd=0,fg='black')
contactnumberEntry.place(x=580,y=280)
contactnumberEntry.insert(0,'')

frame2=Frame(forgot_password_window,width=250,height=2,bg='#57a1f8')
frame2.place(x=580,y=302)




password=Label(forgot_password_window,text='New Password',font=('Microsoft Yahei UI',11,'bold'),bd=0,fg='#57a1f8',bg='white')
password.place(x=580,y=325)

passwordEntry=Entry(forgot_password_window,width=25,font=('Microsoft Yahei UI',11),bd=0,fg='black')
passwordEntry.place(x=580,y=355)
passwordEntry.insert(0,'')

frame3=Frame(forgot_password_window,width=250,height=2,bg='#57a1f8')
frame3.place(x=580,y=377)


openeye=PhotoImage(file='open.png')
eyeButton=Button(forgot_password_window,image=openeye,bd=0,bg='white',activebackground='white',
                 cursor='hand2',command=show)
eyeButton.place(x=800,y=349)


back1=PhotoImage(file='back.png')
backButton=Button(forgot_password_window,image=back1,bd=0,bg='#ade8f2',activebackground='#ade8f2',
                 cursor='hand2',command=back)
backButton.place(x=104,y=68)

confirmpassword=Label(forgot_password_window,text='Confirm New Password',font=('Microsoft Yahei UI',11,'bold'),bd=0,fg='#57a1f8',bg='white')
confirmpassword.place(x=580,y=400)

confirmpasswordEntry=Entry(forgot_password_window,width=25,font=('Microsoft Yahei UI',11),bd=0,fg='black')
confirmpasswordEntry.place(x=580,y=430)
confirmpasswordEntry.insert(0,'')

frame4=Frame(forgot_password_window,width=250,height=2,bg='#57a1f8')
frame4.place(x=580,y=452)


openeye1=PhotoImage(file='open.png')
eyeButton1=Button(forgot_password_window,image=openeye1,bd=0,bg='white',activebackground='white',
                 cursor='hand2',command=show1)
eyeButton1.place(x=800,y=424)



loginButton=Button(forgot_password_window,text='Change Password',font=('Open Sans',16,'bold'),fg='white',
                   bg='#57a1f8',activeforeground='white',activebackground='#57a1f8',
                   cursor='hand2',bd=0,width=19,command=change_password)

loginButton.place(x=578,y=470)





forgot_password_window.mainloop()

