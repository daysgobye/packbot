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
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()


def key_press(key):
    print(key.name)

keyboard.on_press(key_press)

while True:
    time.sleep(1)
