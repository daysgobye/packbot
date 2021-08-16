
import RPi.GPIO as GPIO
import time
from threading import Thread
GPIO.setmode(GPIO.BCM)



class Roll:
    def __init__(self,pins,name,stepsPerTen):
        self.name = name
        self.pins= pins
        self.stepCount= stepsPerTen
        for pin in self.pins:
            GPIO.setup(pin,GPIO.OUT)
            GPIO.output(pin,0)
    def do_work(self,count):
        seq = [ [1,0,0,0],
                [1,1,0,0],
                [0,1,0,0],
                [0,1,1,0],
                [0,0,1,0],
                [0,0,1,1],
                [0,0,0,1],
                [1,0,0,1] ]
        steps= self.stepCount*count
        for i in range(steps):
            for halfstep in range(8):
                for pin in range(4):
                    GPIO.output(self.pins[pin], seq[halfstep][pin])
                time.sleep(0.001)



    def feed(self, count=1):
        background_thread = Thread(target=self.do_work, args=(count))
        background_thread.start()
 
