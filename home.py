from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import pymysql
import webbrowser





def on_home_button_click():
    webbrowser.open('https://www.university.com/')

def change_settings():
    home_window.destroy()
    import changesettings


def logout():
    home_window.destroy()
    import signin

def moduleclick():
    home_window.destroy()
    import ModuleEnrolment


home_window = Tk()
home_window.resizable(0, 0)
home_window.title('Module Enrolment Page')

bgImage = ImageTk.PhotoImage(file='HOMEE.png')

bgLabel = Label(home_window, image=bgImage)
bgLabel.pack()



home = PhotoImage(file='test1.png')
homeButton = Button(home_window, image=home, bd=0, highlightthickness=0, activebackground='#1697d1',
                    cursor='hand2')
homeButton.place(x=28, y=120)

enrol = PhotoImage(file='enrol.png')
enrolButton = Button(home_window, image=enrol, bd=0, highlightthickness=0, activebackground='#1697d1',
                     cursor='hand2',command=moduleclick)
enrolButton.place(x=19, y=260)

web = PhotoImage(file='web.png')
webButton = Button(home_window, image=web, bd=0, highlightthickness=0, activebackground='#1697d1',
                   cursor='hand2', command=on_home_button_click)
webButton.place(x=30, y=394)

settings = PhotoImage(file='settings.png')
settingsButton = Button(home_window, image=settings, bd=0, highlightthickness=0, activebackground='#1697d1',
                        cursor='hand2',command=change_settings)
settingsButton.place(x=28, y=526)

LogoutButton=Button(home_window,text='Logout',font=('Open Sans bold',10,'bold'),fg='white',
                   bg='#1697d1',activeforeground='white',activebackground='#1697d1',
                   cursor='hand2',bd=0,command=logout)
LogoutButton.place(x=838,y=560)

home_window.mainloop()