from roll import Roll
from screen import Screen
from pynput import keyboard
def on_press(key):
    print('{0} pressed'.format(
        key.char))

def on_release(key):
    print('{0} release'.format(
        key.char))
    if key == Key.esc:
        # Stop listener
        return False

# Collect events until released

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
