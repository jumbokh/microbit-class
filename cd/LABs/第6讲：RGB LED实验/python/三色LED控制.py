from microbit import *

"""
 自定义一个RGB LED函数
"""
def RGB_LED(red,green,blue,nms):
    i_red = red * 4
    i_green = green *4
    i_blue = blue * 4
    pin0.write_analog(i_red)
    pin1.write_analog(i_green)
    pin2.write_analog(i_blue)
    sleep(nms)
    
while True:
    RGB_LED(255,0,0,500)
    RGB_LED(0,255,0,500)
    RGB_LED(0,0,255,500)
    RGB_LED(255,255,0,500)
    RGB_LED(255,0,255,500)
    RGB_LED(192,255,62,500)
    RGB_LED(148,0,211,500)
    RGB_LED(188,238,0,500)
    RGB_LED(0,197,205,500)
    
    