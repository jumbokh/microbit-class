from microbit import *



while True:
    if not pin5.read_digital():
        pin0.write_digital(0)
        pin1.write_digital(1)
    else:
        pin0.write_digital(1)
        pin1.write_digital(0)