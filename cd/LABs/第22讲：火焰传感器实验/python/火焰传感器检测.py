from microbit import *


while True:
    FireV = pin0.read_analog()
    if FireV < 100:  #������ֵ�жϣ����ֵԽ��������Խ��
        display.scroll('Fire!')
    else:
        display.scroll('safe~')
        