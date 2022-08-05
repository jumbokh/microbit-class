from microbit import * #导入microbit操作库

while True:
    pin0.write_digital(1) #红色灯点亮
    pin1.write_digital(0) #绿灯熄灭
    sleep(1000) #延时1s
    pin0.write_digital(0) #红色灯熄灭
    pin1.write_digital(1) #绿色灯点亮
    sleep(1000) #延时1s
    
    