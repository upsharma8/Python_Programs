#line
#oval
#polygon
#arc

import tkinter
from tkinter import *
t=Tk()
C=Canvas(t,bg='blue',height=250, width=300)

line=C.create_line(10,10,200,200,fill='white')
#oval=C.create_oval(10,10,200,200,fill='green')
#polygon=C.create_polygon(10,10,100,100,300,300,fill='red')

arc=C.create_arc(10,50,250,220,fill='red')

C.pack()
t.mainloop

#Create a login activity if username and password correct then welocme
#create a calculator
