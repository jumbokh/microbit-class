from microbit import *

global state

def direction():
    state = ['home','up','down','left','rigth','pressed']
    i = 0
    if pin0.read_analog() <= 20:
        i = 1   #up
    if pin0.read_analog() >= 1000:
        i = 2   #down
    if pin1.read_analog() >= 1000:
        i = 3   #left
    if pin1.read_analog() <= 50:
        i = 4   #right
    if pin2.read_analog() <= 20:
       i =  5   #Button pressed 
    return state[i]
    
    
status = ''
while True:
    tmp = direction()
    if tmp !=None and tmp !=status:
        display.scroll(tmp)
        status = tmp
         