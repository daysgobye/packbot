#!/usr/bin/python
# -*- coding: utf-8 -*-

from roll import Roll
from Tkinter  import *

root = Tk()

axisx = [4,17,27,22]
axisy = [10,9,11,7]
axisz = [15,18,23,24]
diode=Roll(axisx,"Diode",100)
rolls=[diode]

for i,roll in enumerate(rolls):
    button1= Button(root,text=roll.name+" x1" ,command=diode.feed)
    button4= Button(root,text=roll.name+" x4" ,command=lambda: diode.feed(4))
    button5= Button(root,text=roll.name+" x5" ,command=lambda: diode.feed(5))
    button6= Button(root,text=roll.name+" x6" ,command=lambda: diode.feed(6))
    button1.grid(column=i)
    button4.grid(column=i)
    button5.grid(column=i)
    button6.grid(column=i)
    

Tk.mainloop(root)

