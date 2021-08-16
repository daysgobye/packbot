import board
import busio
import digitalio
import adafruit_ssd1306
from PIL import Image, ImageDraw, ImageFont

class Screen:
    def __init__(self):
        self.BORDER = 5
        self.oled_reset = digitalio.DigitalInOut(board.D4)
        self.i2c = board.I2C()
        self.oled = adafruit_ssd1306.SSD1306_I2C(128, 32, self.i2c, addr=0x3C)
        self.font = ImageFont.load_default()
        self.clear()

    def clear(self):
        self.oled.fill(0)
        self.oled.show()

    def print_text(self,text):
        self.clear()
        self.image = Image.new("1", (self.oled.width, self.oled.height))
        self.draw = ImageDraw.Draw(self.image)
        (font_width, font_height) = self.font.getsize(text)
        self.draw.text(
        (self.oled.width // 2 - font_width // 2, self.oled.height // 2 - font_height // 2),
        text,
        font=self.font,
        fill=255,
        )

        self.oled.image(self.image)
        self.oled.show()

