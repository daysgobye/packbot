import board
import busio
import digitalio
import adafruit_ssd1306
from PIL import Image, ImageDraw, ImageFont

class Screen:
    def __init__(self):
        self.text=["","","",""]
        self.BORDER = 5
        self.oled_reset = digitalio.DigitalInOut(board.D4)
        self.i2c = board.I2C()
        self.oled = adafruit_ssd1306.SSD1306_I2C(128, 32, self.i2c, addr=0x3C)
        self.font = ImageFont.load_default()
        self.clear()

    def clear(self):
        self.oled.fill(0)
        self.oled.show()
        self.text=["","",""]

    def print_text(self,newText,lineNumber):
        self.text[lineNumber]=newText 
        self.image = Image.new("1", (self.oled.width, self.oled.height))
        self.draw = ImageDraw.Draw(self.image)
        self.draw.text(
        (0,0),
        self.text[0],
        font=self.font,
        fill=255,
        )
        self.draw.text(
        (0,15),
        self.text[1],
        font=self.font,
        fill=255,
        )
        self.draw.text(
        (0,30),
        self.text[2],
        font=self.font,
        fill=255,
        )
        self.oled.image(self.image)
        self.oled.show()

