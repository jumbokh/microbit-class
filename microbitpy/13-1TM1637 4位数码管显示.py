from microbit import *
import TM1637

tm = TM1637.TM1637(dio=pin14,clk=pin13)

n = 0
while True:
    tm.shownum(n)
    n += 1  #n = n + 1
    sleep(1000)
    
"""    
    tm.showbit(1,0)
    tm.showbit(2,1)
    tm.showbit(3,2)
    tm.showbit(0,3)
    sleep(1000)
    tm.showbit(1,0)
    tm.showbit(1,1)
    tm.showbit(2,2)
    tm.showbit(0,3)
    sleep(1000)   
""" 

    