from microbit import * #����microbit������

while True:
    pin0.write_digital(1) #��ɫ�Ƶ���
    pin1.write_digital(0) #�̵�Ϩ��
    sleep(1000) #��ʱ1s
    pin0.write_digital(0) #��ɫ��Ϩ��
    pin1.write_digital(1) #��ɫ�Ƶ���
    sleep(1000) #��ʱ1s
    
    