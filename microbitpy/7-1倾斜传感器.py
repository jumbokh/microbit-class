from microbit import *


while True:
    if pin5.read_digital():#被挡住了
        pin0.write_digital(0)
        pin1.write_digital(1)
    else:  #没有被挡住
        pin0.write_digital(1)
        pin1.write_digital(0)        