from microbit import *
import math

status = 1
tmp = 1

while True:
    analogVal = pin0.read_analog()
    Vr = 3.3 * float(analogVal)/1023
    Rt = 10000 * Vr / (3.3-Vr)
    temp = 1/(((math.log(Rt / 10000)) / 3950) + (1 / (273.15+25)))
    temp = temp - 273.15
    display.scroll(str(round(temp,2)))
    