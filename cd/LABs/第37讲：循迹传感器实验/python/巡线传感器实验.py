from microbit import *

while True:
    if not pin5.read_digital():
        display.scroll('White!')
    else:
        display.scroll('Black!')
        
    