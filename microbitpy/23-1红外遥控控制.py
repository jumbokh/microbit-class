from microbit import *
import necir

def cb(addr,cmd):
  if cmd == 0xba45:
    pin0.write_digital(1)
    pin1.write_digital(0)
    pin2.write_digital(0)
  elif cmd == 0xb946:
    pin0.write_digital(0)
    pin1.write_digital(1)
    pin2.write_digital(0) 
  elif cmd == 0xb847:
    pin0.write_digital(0)
    pin1.write_digital(0)
    pin2.write_digital(1)
    
  print('addr=',hex(addr)) #打印键值
  print('cmd=',hex(cmd))  
  

necir.init(16)
necir.read(cb)
#write your program:

while True:
  pass

