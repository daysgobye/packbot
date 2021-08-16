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
    display.print_text("feed amt: "+str(feedAmt),1)

keyboard.on_press(key_press)

while True:
    time.sleep(1)
