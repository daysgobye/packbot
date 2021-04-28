#!/usr/bin/python
# -*- coding: utf-8 -*-

from roll import Roll
from Tkinter  import *

root = Tk()

axisx = [4,17,27,22]
axisy = [10,9,11,7]
axisz = [15,18,23,24]

diode=Roll(axisx,"Diode",100)

diodeButton1= Button(root,text="diode x1" ,command=diode.feed)
diodeButton2= Button(root,text="diode x2", command= lambda: diode.feed(2))
diodeButton5= Button(root,text="diode x5", command= lambda: diode.feed(5))
diodeButton6= Button(root,text="diode x6", command= lambda: diode.feed(6))
diodeButton1.pack()
diodeButton2.pack()
diodeButton5.pack()
diodeButton6.pack()
    

Tk.mainloop(root)

