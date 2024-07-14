from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import pymysql
import webbrowser


def remove_account():
    registration_number_to_remove = registrationnumberEntry.get()
    result = messagebox.askquestion("Warning", f"Are you sure you want to remove the account with registration number {registration_number_to_remove}?")
    if result == 'yes':
        remove_data(registration_number_to_remove)
    else:
        print("User clicked 'No' or closed the messagebox")


def remove_data(registration_number):
    if registrationnumberEntry.get()=='' or registrationnumberEntry.get()==' ':
        messagebox.showerror('Error', 'Please enter Your Registration Number')
    else:
        try:
            con = pymysql.connect(host='localhost', user='root', password='Evo9Jw2474', database='studentdata')
            mycursor = con.cursor()

            query = 'select * from data where registration_number=%s'
            mycursor.execute(query, (registration_number,))
            row = mycursor.fetchone()

            if row is None:
                messagebox.showerror('Error', 'Invalid Registration number')
            else:
                query = 'delete from data where registration_number=%s'
                mycursor.execute(query, (registration_number,))
                con.commit()
                con.close()
                messagebox.showinfo('Success', 'Account Removed Successfully')
                settings_window.destroy()

        except Exception as e:
            messagebox.showerror('Error', f'Error: {str(e)}')



def change_settings():


    if registrationnumberEntry.get()=='' or registrationnumberEntry.get()==' ':
        messagebox.showerror('Error', 'Please enter Your Registration Number')

    elif firstnameEntry1.get() == '' or lastnameEntry1.get() == '' or contactnumberEntry1.get() == '' or addressEntry1.get() == '' or passwordEntry1.get() == '' or confirmpasswordEntry1.get() == '':
        messagebox.showerror('Error', 'Please fill the all details')

    elif confirmpasswordEntry1.get() != passwordEntry1.get():
        messagebox.showerror('Error', 'Passwords do not match. Please double-check and try again')

    else:
        con = pymysql.connect(host='localhost', user='root', password='Evo9Jw2474', database='studentdata')
        mycursor = con.cursor()
        query = 'select * from data where registration_number=%s'
        mycursor.execute(query, (registrationnumberEntry.get()))
        row = mycursor.fetchone()

        if row == None:
            messagebox.showerror('Error', 'Invalid Registration number')
        else:
            query = 'update data set password=%s, first_name=%s, last_name=%s, contact_number=%s, address=%s where registration_number=%s'
            mycursor.execute(query, (
            passwordEntry1.get(), firstnameEntry1.get(), lastnameEntry1.get(), contactnumberEntry1.get(),
            addressEntry1.get(), registrationnumberEntry.get()))
            con.commit()
            con.close()
            messagebox.showinfo('Success', 'Profile Settings has been Changed')


def on_home_button_click():
    webbrowser.open('https://www.university.com/')




def moduleclick():
    settings_window.destroy()
    import ModuleEnrolment


def home_click():
    settings_window.destroy()
    import home


def hide():
    openeye.config(file='close.png')
    passwordEntry1.config(show='\u2022')
    eyeButton.config(command=show)


def show():
    openeye.config(file='open.png')
    passwordEntry1.config(show='')
    eyeButton.config(command=hide)


def hide1():
    openeye1.config(file='close.png')
    confirmpasswordEntry1.config(show='\u2022')
    eyeButton1.config(command=show1)


def show1():
    openeye1.config(file='open.png')
    confirmpasswordEntry1.config(show='')
    eyeButton1.config(command=hide1)


settings_window = Tk()
settings_window.resizable(0, 0)
settings_window.title('Module Enrolment Page')

bgImage = ImageTk.PhotoImage(file='changeprofile.png')

bgLabel = Label(settings_window, image=bgImage)
bgLabel.pack()

heading = Label(settings_window, text='Change Account Settings', font=('Microsoft Yahei UI bold', 22, 'bold'), bd=0,
                fg='black', bg='white')
heading.place(x=330, y=120)

home = PhotoImage(file='test1.png')
homeButton = Button(settings_window, image=home, bd=0, highlightthickness=0, activebackground='#1697d1',
                    cursor='hand2', command=home_click)
homeButton.place(x=28, y=120)

enrol = PhotoImage(file='enrol.png')
enrolButton = Button(settings_window, image=enrol, bd=0, highlightthickness=0, activebackground='#1697d1',
                     cursor='hand2', command=moduleclick)
enrolButton.place(x=19, y=260)

web = PhotoImage(file='web.png')
webButton = Button(settings_window, image=web, bd=0, highlightthickness=0, activebackground='#1697d1',
                   cursor='hand2', command=on_home_button_click)
webButton.place(x=30, y=394)

settings = PhotoImage(file='settings.png')
settingsButton = Button(settings_window, image=settings, bd=0, highlightthickness=0, activebackground='#1697d1',
                        cursor='hand2')
settingsButton.place(x=28, y=526)

frame = Frame(settings_window, bg='white')
frame.place(x=182, y=250)

firstnameLabel = Label(frame, text='First Name :', font=('Microsoft Yahei UI', 10, 'bold'), bg='white', fg='#57a1f8')
firstnameLabel.grid(row=0, column=0, sticky='w', padx=25, pady=10)

firstnameEntry1 = Entry(frame, width=35, font=('Microsoft Yahei UI', 10), fg='black')
firstnameEntry1.grid(row=2, column=0, sticky='w', padx=25)

firstnameEntry1.insert(0, 'First Name')

lastnameLabel = Label(frame, text='Last Name :', font=('Microsoft Yahei UI', 10, 'bold'), bg='white', fg='#57a1f8')
lastnameLabel.grid(row=0, column=2, sticky='w', padx=55, pady=10)

lastnameEntry1 = Entry(frame, width=35, font=('Microsoft Yahei UI', 10), fg='black')
lastnameEntry1.grid(row=2, column=2, sticky='w', padx=55)

lastnameEntry1.insert(0, 'Last Name')

contactnumberLabel = Label(frame, text='Contact Number :', font=('Microsoft Yahei UI', 10, 'bold'), bg='white',
                           fg='#57a1f8')
contactnumberLabel.grid(row=3, column=0, sticky='w', padx=25, pady=10)

contactnumberEntry1 = Entry(frame, width=35, font=('Microsoft Yahei UI', 10), fg='black')
contactnumberEntry1.grid(row=4, column=0, sticky='w', padx=25)

contactnumberEntry1.insert(0, 'Contact Number')

addressLabel = Label(frame, text='Address :', font=('Microsoft Yahei UI', 10, 'bold'), bg='white', fg='#57a1f8')
addressLabel.grid(row=3, column=2, sticky='w', padx=55, pady=10)

addressEntry1 = Entry(frame, width=35, font=('Microsoft Yahei UI', 10), fg='black')
addressEntry1.grid(row=4, column=2, sticky='w', padx=55)

addressEntry1.insert(0, 'Address')

passwordLabel = Label(frame, text='Password :', font=('Microsoft Yahei UI', 10, 'bold'), bg='white', fg='#57a1f8')
passwordLabel.grid(row=5, column=0, sticky='w', padx=25, pady=10)

passwordEntry1 = Entry(frame, width=35, font=('Microsoft Yahei UI', 10), fg='black')
passwordEntry1.grid(row=6, column=0, sticky='w', padx=25)

passwordEntry1.insert(0, 'New Password')

confirmpasswordLabel = Label(frame, text='Confirm Password :', font=('Microsoft Yahei UI', 10, 'bold'), bg='white',
                             fg='#57a1f8')
confirmpasswordLabel.grid(row=5, column=2, sticky='w', padx=55, pady=10)

confirmpasswordEntry1 = Entry(frame, width=35, font=('Microsoft Yahei UI', 10), fg='black')
confirmpasswordEntry1.grid(row=6, column=2, sticky='w', padx=55)

confirmpasswordEntry1.insert(0, 'Confirm New Password')


registrationnumberLabel = Label(settings_window, text='Your Registration Number : ', font=('Microsoft Yahei UI bold', 10, 'bold'), bg='white',
                             fg='#57a1f8')
registrationnumberLabel.place(x=280, y=190)

registrationnumberEntry = Entry(settings_window, width=35, font=('Microsoft Yahei UI bold', 10), fg='black')
registrationnumberEntry.place(x=480, y=190)

registrationnumberEntry.insert(0, 'EG/')


openeye = PhotoImage(file='open.png')
eyeButton = Button(settings_window, image=openeye, bd=0, bg='white', activebackground='white',
                   cursor='hand2', command=hide)
eyeButton.place(x=465, y=432)

openeye1 = PhotoImage(file='open.png')
eyeButton1 = Button(settings_window, image=openeye1, bd=0, bg='white', activebackground='white',
                    cursor='hand2', command=hide1)
eyeButton1.place(x=825, y=432)

submitButton = Button(text='Update', font=('Microsoft Yahei UI Bold', 16, 'bold'), bd=0, bg='#57a1f8', fg='white',
                      activebackground='#57a1f8', activeforeground='white', width='17', cursor='hand2',
                      command=change_settings)
submitButton.place(x=390, y=490)

removeButton=Button(settings_window,text='Remove My Account',font=('Open Sans',10,'bold'),fg='black',
                   bg='#e80000',activeforeground='black',activebackground='#e80000',
                   cursor='hand2',bd=0,command=remove_account)
removeButton.place(x=762,y=555)

settings_window.mainloop()