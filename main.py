from roll import Roll
from screen import Screen
display=Screen()
display.print_text("test")
set1= [4,17,27,22]
led1=Roll(set1,"MINI-E",100)
led1.feed(20)
