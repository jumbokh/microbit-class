from microbit import *



while True:
    display.scroll(str(pin0.read_analog()))