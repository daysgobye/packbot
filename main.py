#!/usr/bin/python
# -*- coding: utf-8 -*-

from roll import Roll
from Tkinter  import *

root = Tk()
keysBinds=[
    ["F1","F7","F13","F19"],
    ["F2","F8","F14","F20"],
    ["F3","F9","F15","F21"],
    ["F4","F10","F16","F22"],
    ["F5","F11","F17","F23"],
    ["F6","F12","F18","F24"],
]
set1= [4,17,27,22]
set2 = [10,9,11,7]
set3 = [15,18,23,24]
set4= [12,16,20,21]
set5= [6,13,19,26]
set6= [5,3,2,14]

led1=Roll(set1,"MINI-E",100)
led2=Roll(set2,"SX-MINI",100)
mx=Roll(set3,"Mx",400)
diode=Roll(set4,"Diode",100)
choc=Roll(set5,"Choc",400)
led3=Roll(set6,"SX-50-50",100)


rolls=[
    led1,
    led2,
    led3,
    mx,
    choc,
    diode,
]

for i,roll in enumerate(rolls):
    button1= Button(root,text=roll.name+" x1" ,command=roll.feed)
    button4= Button(root,text=roll.name+" x4" ,command=lambda: roll.feed(4))
    button5= Button(root,text=roll.name+" x5" ,command=lambda: roll.feed(5))
    button6= Button(root,text=roll.name+" x6" ,command=lambda: roll.feed(6))
    button1.grid(row=1,column=i)
    button4.grid(row=2,column=i)
    button5.grid(row=3,column=i)
    button6.grid(row=4,column=i)
for roll in rolls:
    print(roll.name)
    roll.feed(10)


Tk.mainloop(root)

