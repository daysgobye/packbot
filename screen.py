import board
import busio
import digitalio
import adafruit_ssd1306
from PIL import Image, ImageDraw, ImageFont

# BORDER = 5
# oled_reset = digitalio.DigitalInOut(board.D4)
# i2c = board.I2C()
# oled = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c, addr=0x3C)

# # Clear display.
# oled.fill(0)
# oled.show()

# # Create blank image for drawing.
# # Make sure to create image with mode '1' for 1-bit color.
# image = Image.new("1", (oled.width, oled.height))

# # Get drawing object to draw on image.
# draw = ImageDraw.Draw(image)

# # Draw a white background
# draw.rectangle((0, 0, oled.width, oled.height), outline=255, fill=255)

# # Draw a smaller inner rectangle
# draw.rectangle(
    # (BORDER, BORDER, oled.width - BORDER - 1, oled.height - BORDER - 1),
    # outline=0,
    # fill=0,
# )

# # Load default font.
# font = ImageFont.load_default()

# # Draw Some Text
# text = "Hello World!"
# (font_width, font_height) = font.getsize(text)
# draw.text(
    # (oled.width // 2 - font_width // 2, oled.height // 2 - font_height // 2),
    # text,
    # font=font,
    # fill=255,
# )

# # Display image
# oled.image(image)
# oled.show()
class Screen:
    def __init__(self):
        self.BORDER = 5
        self.oled_reset = digitalio.DigitalInOut(board.D4)
        self.i2c = board.I2C()
        self.oled = adafruit_ssd1306.SSD1306_I2C(128, 32, self.i2c, addr=0x3C)
        self.font = ImageFont.load_default()
        self.image = Image.new("1", (self.oled.width, self.oled.height))
        self.draw = ImageDraw.Draw(self.image)
        self.clear()

    def clear(self):
        self.oled.fill(0)
        self.oled.show()

    def print_text(self,text):
        (font_width, font_height) = font.getsize(text)
        self.draw.text(
        (self.oled.width // 2 - font_width // 2, self.oled.height // 2 - font_height // 2),
        text,
        font=self.font,
        fill=255,
        )
        self.oled.show()

