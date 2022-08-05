from microbit import *


while True:
    if not pin5.read_digital():  # 没有按下的时候为1，not 为0，就会执行else的代码，按下的时候为0，not为1了 这样子就执行if语句的代码
        pin0.write_digital(0)
        pin1.write_digital(1)
    else:  #按键按下
        pin0.write_digital(1)
        pin1.write_digital(0)        