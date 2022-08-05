from microbit import * 

while True:
    pin0.write_analog(1023) #在P0口上输出3.3V
    pin1.write_analog(0)
    sleep(500)
    pin0.write_analog(0) #在P0口上输出0V
    pin1.write_analog(1023)
    sleep(500)
    pin0.write_analog(1023) #在P0口上输出3.3V
    pin1.write_analog(511)
    sleep(500)
    pin0.write_analog(1023) #在P0口上输出3.3V
    pin1.write_analog(1023)
    sleep(500)
    pin0.write_analog(511) #在P0口上输出1.65V
    pin1.write_analog(1023)
    sleep(500)    