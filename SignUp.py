from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import pymysql

#functions


def clear():
    emailEntry.delete(0,END)
    registrationnumberEntry.delete(0, END)
    passwordEntry.delete(0, END)
    confirmpasswordEntry.delete(0, END)
    firstnameEntry.delete(0, END)
    lastnameEntry.delete(0, END)
    contactnumberEntry.delete(0, END)
    addressEntry.delete(0, END)
    check.set(0)


def login_page():
    SignUp_window.destroy()
    import signin

def connect_database():
    if firstnameEntry.get()==''  or lastnameEntry.get()=='' or contactnumberEntry.get()=='' or addressEntry.get()=='' or passwordEntry.get()==''  or emailEntry.get()=='' or registrationnumberEntry.get()=='' or confirmpasswordEntry.get()=='':
        messagebox.showerror('Error','Please fill the all details')
    elif passwordEntry.get() != confirmpasswordEntry.get():
        messagebox.showerror('Error','Passwords do not match. Please double-check and try again')
    elif check.get()==0:
        messagebox.showerror('Error','Please read and agree to our Terms & Condition')

    else:

        try:
            con=pymysql.connect(host='localhost',user='root',password='1234')
            mycursor=con.cursor()
        except:
            messagebox.showerror('Error','Your data was unable to record, Please try Again')
            return

        try:
            query='create database studentdata'
            mycursor.execute(query)
            query='use studentdata'
            mycursor.execute(query)
            query='create table data(id int auto_increment primary key not null, email varchar(50),registration_number varchar(20),password varchar(20),first_name varchar(50),last_name varchar(100),contact_number varchar(10),address varchar(150))'
            mycursor.execute(query)
        except:
            mycursor.execute('use studentdata')

        query='select * from data where registration_number=%s'
        mycursor.execute(query,(registrationnumberEntry.get()))

        row=mycursor.fetchone()
        if row!=None:
            messagebox.showerror('Error', 'You have already registered to the System')

        else:
            query = 'insert into data(email,registration_number,password,first_name,last_name,contact_number,address) values(%s,%s,%s,%s,%s,%s,%s)'
            mycursor.execute(query, (
            emailEntry.get(), registrationnumberEntry.get(), passwordEntry.get(), firstnameEntry.get(),
            lastnameEntry.get(), contactnumberEntry.get(), addressEntry.get()))
            con.commit()
            con.close()
            messagebox.showinfo('Success', 'You have successfully Registered to the System')
            clear()
            SignUp_window.destroy()
            import signin















#UI

SignUp_window=Tk()
SignUp_window.resizable(0,0)
SignUp_window.title('SignUp Window')
background=ImageTk.PhotoImage(file='registerback.png')
backgroundlabel=Label(SignUp_window,image=background)
backgroundlabel.grid()

frame=Frame(SignUp_window,bg='white' )
frame.place(x=132,y=130)



firstnameLabel=Label(frame,text='First Name',font=('Microsoft Yahei UI',10,'bold'),bg='white',fg='#57a1f8')
firstnameLabel.grid(row=0,column=0,sticky='w',padx=25,pady=10)

firstnameEntry=Entry(frame,width=35,font=('Microsoft Yahei UI',10),fg='black')
firstnameEntry.grid(row=2,column=0,sticky='w',padx=25)

lastnameLabel=Label(frame,text='Last Name',font=('Microsoft Yahei UI',10,'bold'),bg='white',fg='#57a1f8')
lastnameLabel.grid(row=0,column=2,sticky='w',padx=55,pady=10)

lastnameEntry=Entry(frame,width=35,font=('Microsoft Yahei UI',10),fg='black')
lastnameEntry.grid(row=2,column=2,sticky='w',padx=55)

contactnumberLabel=Label(frame,text='Contact Number',font=('Microsoft Yahei UI',10,'bold'),bg='white',fg='#57a1f8')
contactnumberLabel.grid(row=3,column=0,sticky='w',padx=25,pady=10)

contactnumberEntry=Entry(frame,width=35,font=('Microsoft Yahei UI',10),fg='black')
contactnumberEntry.grid(row=4,column=0,sticky='w',padx=25)

addressLabel=Label(frame,text='Address',font=('Microsoft Yahei UI',10,'bold'),bg='white',fg='#57a1f8')
addressLabel.grid(row=3,column=2,sticky='w',padx=55,pady=10)

addressEntry=Entry(frame,width=35,font=('Microsoft Yahei UI',10),fg='black')
addressEntry.grid(row=4,column=2,sticky='w',padx=55)




registrationnumberLabel=Label(frame,text='Registration Number',font=('Microsoft Yahei UI',10,'bold'),bg='white',fg='#57a1f8')
registrationnumberLabel.grid(row=5,column=0,sticky='w',padx=25,pady=10)

registrationnumberEntry=Entry(frame,width=35,font=('Microsoft Yahei UI',10),fg='black')
registrationnumberEntry.grid(row=6,column=0,sticky='w',padx=25)


emailLabel=Label(frame,text='Email',font=('Microsoft Yahei UI',10,'bold'),bg='white',fg='#57a1f8')
emailLabel.grid(row=5,column=2,sticky='w',padx=55,pady=10)

emailEntry=Entry(frame,width=35,font=('Microsoft Yahei UI',10),fg='black')
emailEntry.grid(row=6,column=2,sticky='w',padx=55)


passwordLabel=Label(frame,text='Password',font=('Microsoft Yahei UI',10,'bold'),bg='white',fg='#57a1f8')
passwordLabel.grid(row=7,column=0,sticky='w',padx=25,pady=10)

passwordEntry=Entry(frame,width=35,font=('Microsoft Yahei UI',10),fg='black')
passwordEntry.grid(row=8,column=0,sticky='w',padx=25)

confirmpasswordLabel=Label(frame,text='Confirm Password',font=('Microsoft Yahei UI',10,'bold'),bg='white',fg='#57a1f8')
confirmpasswordLabel.grid(row=7,column=2,sticky='w',padx=55,pady=10)

confirmpasswordEntry=Entry(frame,width=35,font=('Microsoft Yahei UI',10),fg='black')
confirmpasswordEntry.grid(row=8,column=2,sticky='w',padx=55)


check=IntVar()
termsandconditions=Checkbutton(text='I agree to the Terms & Conditions', font=('Microsoft Yahei UI',8) , bg='white', fg='firebrick1' , activebackground='white' , activeforeground='firebrick1' , cursor='hand2',variable=check)
termsandconditions.place(x=380,y=420)

signupButton=Button(text='SignUp', font=('Microsoft Yahei UI Bold',16,'bold') , bd=0 , bg='#57a1f8' , fg='white', activebackground='#57a1f8' , activeforeground='white',width='17',command=connect_database )
signupButton.place(x=360,y=460)


alreadyaccountLabel=Label(text='Already have an Account',font=('Microsoft Yahei UI',10),bg='white',fg='firebrick1')
alreadyaccountLabel.place(x=365,y=520)

loginButton=Button(text='Login', font=('Microsoft Yahei UI Bold',10,'underline') , bd=0 , bg='white' ,cursor='hand2', fg='#57a1f8', activebackground='white' , activeforeground='#57a1f8' ,command=login_page)
loginButton.place(x=530,y=517)


SignUp_window.mainloop()