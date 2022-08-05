from microbit import *

def digitalRead(pin):
  pin.read_digital()
  return pin.read_digital()


while True:
  if digitalRead(pin5):
    pin0.write_digital(0)
    pin1.write_digital(1)
  else:
    pin0.write_digital(1)
    pin1.write_digital(0)