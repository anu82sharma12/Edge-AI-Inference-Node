from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306
import board
import busio

i2c = busio.I2C(board.SCL, board.SDA)
oled = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c)

def show_oled(label, latency):
    image = Image.new("1", (128, 32))
    draw = ImageDraw.Draw(image)
    draw.text((0, 0), label[:15], fill=255)
    draw.text((0, 16), latency, fill=255)
    oled.image(image)
    oled.show()
