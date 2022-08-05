from microbit import *

# Write your code here :-)
while True:
    if pin0.read_digital() == 0:
        pin5.write_digital(0)
        display.scroll('Danger Gas!!!')
    else:
        pin5.write_digital(1)
        display.scroll('safe~')
        