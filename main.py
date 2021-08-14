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
feedAmt=1
def key_press(e):
    code=e.char
    if code=="q":
       feedAmt+=1
    if code=="w":
       feedAmt-=1
    if code =="e":
       feedAmt+=10
    if code =="r":
       feedAmt-=10
    if code =="t":
       feedAmt=1
    if code=="a":
       led1.feed(feedAmt)
    if code=="s":
        led2.feed(feedAmt)
    if code=="d":
        led3.feed(feedAmt)
    if code=="f":
        mx.feed(feedAmt)
    if code =="g":
        choc.feed(feedAmt)
    if code=="h":
        diode.feed(feedAmt)
    if code=="z":
        led1.feed(1)
    if code=="x":
        led2.feed(1)
    if code=="c":
        led3.feed(1)
    if code=="v":
        mx.feed(1)
    if code=="b":
        choc.feed(1)
    if code=="n":
        diode.feed(1)
    if code=="u":
        led1.feed(6)
    if code=="j":
        led2.feed(6)
    if code=="m":
        led3.feed(6)
    if code=="i":
        mx.feed(6)
    if code=="k":
        choc.feed(6)
    if code=="o":
        diode.feed(6)


rolls=[
    led1,
    led2,
    led3,
    mx,
    choc,
    diode,
]
add1=Button(root,text="+1")
sub1=Button(root,text="-1")
add10=Button(root,text="+10")
sub10=Button(root,text="-10")
reset=Button(root,text="rest")
feedview=Label(root, text="("+feedAmt+")")
add1.grid(row=1,column=0)
sub1.grid(row=1,column=1)
add10.grid(row=1,column=2)
sub10.grid(row=1,column=3)
reset.grid(row=1,column=4)
feedview.grid(row=1,column=5)

for i,roll in enumerate(rolls):
    button1= Button(root,text=roll.name+" x"+feedAmt ,command=roll.feed)
    button4= Button(root,text=roll.name+" x1" ,command=lambda: roll.feed(4))
    button6= Button(root,text=roll.name+" x6" ,command=lambda: roll.feed(6))
    button1.grid(row=3,column=i)
    button4.grid(row=4,column=i)
    button6.grid(row=5,column=i)


root.bind("<Key>",key_press)

Tk.mainloop(root)

