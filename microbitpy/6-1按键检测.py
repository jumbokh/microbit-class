from microbit import *


while True:
    if not pin5.read_digital():  # û�а��µ�ʱ��Ϊ1��not Ϊ0���ͻ�ִ��else�Ĵ��룬���µ�ʱ��Ϊ0��notΪ1�� �����Ӿ�ִ��if���Ĵ���
        pin0.write_digital(0)
        pin1.write_digital(1)
    else:  #��������
        pin0.write_digital(1)
        pin1.write_digital(0)        