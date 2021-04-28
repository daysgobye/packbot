#!/usr/bin/python
# -*- coding: utf-8 -*-

from roll import Roll
import tkinter as tk

axisx = [4,17,27,22]
axisy = [10,9,11,7]
axisz = [15,18,23,24]

diode=Roll(axisx,"Diode",100)

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.diodeButton1= tk.Button(self,text="diode x1" command=diode.feed)
        self.diodeButton2= tk.Button(self,text="diode x2" command= lambda: diode.feed(2))
        self.diodeButton5= tk.Button(self,text="diode x5" command= lambda: diode.feed(5))
        self.diodeButton6= tk.Button(self,text="diode x6" command= lambda: diode.feed(6))
        self.diodeButton1.pack()
        self.diodeButton2.pack()
        self.diodeButton5.pack()
        self.diodeButton6.pack()


        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

    

root = tk.Tk()
app = Application(master=root)
app.mainloop()

except KeyboardInterrupt:
  print "  Quit"
  GPIO.cleanup()
