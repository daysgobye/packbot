from roll import Roll
from screen import Screen
import keyboard
import time

display=Screen()
set1= [4,17,27,22]
set2 = [10,9,11,7]
set3 = [15,18,23,24]
set4= [12,16,20,21]
set5= [6,13,19,26]
set6= [5,25,8,14]


led1=Roll(set1,"MINI-E",100)
led2=Roll(set2,"SX-MINI",100)
mx=Roll(set3,"Mx",400)
diode=Roll(set4,"Diode",100)
choc=Roll(set5,"Choc",400)
led3=Roll(set6,"SX-50-50",100)
feedAmt=1
def key_press(key):
    global feedAmt
    code=key.name
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
       led1.start(feedAmt)
    if code=="s":
        led2.start(feedAmt)
    if code=="d":
        led3.start(feedAmt)
    if code=="f":
        mx.start(feedAmt)
    if code =="g":
        choc.start(feedAmt)
    if code=="h":
        diode.start(feedAmt)
    if code=="z":
        led1.start(1)
    if code=="x":
        led2.start(1)
    if code=="c":
        led3.start(1)
    if code=="v":
        mx.start(1)
    if code=="b":
        choc.start(1)
    if code=="n":
        diode.start(1)
    if code=="u":
        led1.start(6)
    if code=="j":
        led2.start(6)
    if code=="m":
        led3.start(6)
    if code=="i":
        mx.start(6)
    if code=="k":
        choc.start(6)
    if code=="o":
        diode.start(6)
    display.print_text(str(feedAmt))

keyboard.on_press(key_press)

while True:
    time.sleep(1)
