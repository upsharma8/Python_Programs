#tkinter library - GUI
import tkinter
from tkinter import *
from tkinter import messagebox
t=tkinter.Tk()
#Widget code
def callback():
    msg=messagebox.showinfo("Hello World","Welcome")

E1=Entry(t,bd=15)
E1.place(x=30,y=30)
    
B=Button(t,text='hello',command=callback)
C=Button(t,text='1',command=callback)
D=Button(t,text='2',command=callback)
E=Button(t,text='3',command=callback)
F=Button(t,text='4',command=callback)
G=Button(t,text='5',command=callback)
H=Button(t,text='6',command=callback)
I=Button(t,text='7',command=callback)
J=Button(t,text='8',command=callback)
K=Button(t,text='9',command=callback)
B.place(x=50,y=50)
C.place(x=50,y=55)
C.place(x=50,y=55)
C.place(x=50,y=55)
C.place(x=50,y=55)
C.place(x=50,y=55)
t.mainloop()

