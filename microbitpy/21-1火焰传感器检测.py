from microbit import *


while True:
    FireV = pin0.read_analog()
    if FireV < 100:  #火焰阈值判断，这个值越大灵敏度越高
        display.scroll('Fire!')
    else:
        display.scroll('safe~')
        