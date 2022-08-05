from microbit import *
import bmp280

b = bmp280.BMP280() 

while True:
    display.scroll('T:')
    display.scroll(str(b.getTemp()))
    display.scroll('P:')
    display.scroll(str(b.getPress()))
    sleep(500)