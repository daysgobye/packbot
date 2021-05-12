#!/usr/bin/python
# -*- coding: utf-8 -*-

from roll import Roll
from Tkinter  import *

root = Tk()

set1= [4,17,27,22]
set2 = [10,9,11,7]
set3 = [15,18,23,24]
diode=Roll(set1,"Diode",100)
mx=Roll(set2,"Mx",400)
choc=Roll(set3,"Choc",400)
rolls=[set1,set2,set3]

for i,roll in enumerate(rolls):
    button1= Button(root,text=roll.name+" x1" ,command=roll.feed)
    button4= Button(root,text=roll.name+" x4" ,command=lambda: roll.feed(4))
    button5= Button(root,text=roll.name+" x5" ,command=lambda: roll.feed(5))
    button6= Button(root,text=roll.name+" x6" ,command=lambda: roll.feed(6))
    button1.grid(column=i)
    button4.grid(column=i)
    button5.grid(column=i)
    button6.grid(column=i)
    

Tk.mainloop(root)

