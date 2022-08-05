from microbit import *

while True:
    if pin5.read_digital() == 0:
        display.scroll('Detected Barrier!')