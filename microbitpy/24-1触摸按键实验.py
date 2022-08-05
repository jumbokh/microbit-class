from microbit import *


while True:
    if pin0.is_touched() == 0:
        pin1.write_digital(1)
    else:
        pin1.write_digital(0)