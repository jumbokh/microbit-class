from microbit import *


while True:
    if pin5.read_digital():#����ס��
        pin0.write_digital(0)
        pin1.write_digital(1)
    else:  #û�б���ס
        pin0.write_digital(1)
        pin1.write_digital(0)        