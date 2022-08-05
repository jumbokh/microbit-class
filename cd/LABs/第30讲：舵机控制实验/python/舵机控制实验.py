from microbit import *
from servo import Servo

servo1 = Servo(pin2)


while True:
    servo1.write_angle(180*(pin0.read_analog()/1023)) #(0 + (180-0) * (pin0.read_analog()-0) / (1023-0))
    sleep(100)