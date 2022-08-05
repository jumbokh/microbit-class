from microbit import *
#write your program:
import dht11

while True:
  temp,hum = dht11.read(1)
  display.scroll('T:')
  display.scroll(str(temp))
  display.scroll('H:')
  display.scroll(str(hum))
  sleep(1000)
