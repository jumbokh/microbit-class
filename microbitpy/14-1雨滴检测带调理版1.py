from microbit import *

# Write your code here :-)
while True:
    display.scroll(str(pin0.read_analog())) #������ת��Ϊ�ַ���
    if not pin5.read_digital():
        display.scroll('Raining')
    else:
        display.scroll('Not Raining')
    