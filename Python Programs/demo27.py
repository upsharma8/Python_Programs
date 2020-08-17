#check button
import tkinter
from tkinter import *
t=Tk()
cvr1=IntVar()
cvr1=IntVar()

c1= CheckButton(t,text="Python",variable=cvr1,onvalue=1,offvalue=0,height=5,width=20)
c2=CheckButton(t,text="Java",variable=cvr2, onvalue=1, offvalue=0, height=5, width=20)
c1.place(x=20,y=20)

c2.place(x=30,y=20)

t.mainloop()
