from machine import I2C,UART,Pin
from Sengo2 import *
import time

# 等待Sengo2完成操作系统的初始化。此等待时间不可去掉，避免出现Sengo2尚未初始化完毕主控器已经开发发送指令的情况
time.sleep(2)

# 选择UART或者I2C通讯模式，Sengo2出厂默认为I2C模式，短按模式按键可以切换
# 4种UART通讯模式：UART9600（标准协议指令），UART57600（标准协议指令），UART115200（标准协议指令），Simple9600（简单协议指令），
# 参看“简单协议指令”
# https://tosee.readthedocs.io/zh/latest/Common/Protocol/index.html#section-6
#########################################################################################################
# port = UART(2,rx=Pin(16),tx=Pin(17),baudrate=9600)
port = I2C(1,scl=Pin(22),sda=Pin(21),freq=400000)

# Sengo2通讯地址：0x60。如果I2C总线挂接多个设备，请避免出现地址冲突
sengo2 = Sengo2(0x60)
 
err = sengo2.begin(port)
print("sengo2.begin: 0x%x"% err)
 
# 1、算法介绍请参考
# https://tosee.readthedocs.io/zh/latest/Sentry2/Vision/index.html#chapter-vision-20class-index
# 2、sengo2可以同时运行多个算法，但有限制要求
# 3、Sengo/sentry系列产品参数与结果的编号都是从1开始；
# 4、正常使用时，应由主控器发送指令控制Sengo2算法的开启与关闭，而非通过摇杆手动进行操作；
err = sengo2.VisionBegin(sengo2_vision_e.kVision20Classes)
print("sengo2.VisionBegin(sengo2_vision_e.kVision20Classes):0x%x"% err)

while True:
  # Sengo不主动返回检测识别结果，需要主控板发送指令进行读取。读取的流程：首先读取识别结果的数量，接收到指令后，Sengo2会刷新结果数据，如果结果数量不为零，那么主控再发送指令读取结果的相关信息。请务必按此流程构建程序。
    obj_num = (sengo2.GetValue(sengo2_vision_e.kVision20Classes, sentry_obj_info_e.kStatus))
    if obj_num:
        print("Totally %d objects: "%( obj_num ))
        for i in range(1,obj_num+1):
            if (sengo2.GetValue(sengo2_vision_e.kVision20Classes,sentry_obj_info_e.kLabel,i)==class20_label_e.kAirplane):
              print("object#%d: AirPlane, "%(i), end='')
            if (sengo2.GetValue(sengo2_vision_e.kVision20Classes,sentry_obj_info_e.kLabel,i)==class20_label_e.kBicycle):
              print("object#%d: Bicycle, "%(i), end='')
            if (sengo2.GetValue(sengo2_vision_e.kVision20Classes,sentry_obj_info_e.kLabel,i)==class20_label_e.kBird):
              print("object#%d: Bird, "%(i), end='')
            if (sengo2.GetValue(sengo2_vision_e.kVision20Classes,sentry_obj_info_e.kLabel,i)==class20_label_e.kBoat):
              print("object#%d: Boat, "%(i), end='')
            if (sengo2.GetValue(sengo2_vision_e.kVision20Classes,sentry_obj_info_e.kLabel,i)==class20_label_e.kBottle):
              print("object#%d: Bottle, "%(i), end='')
            if (sengo2.GetValue(sengo2_vision_e.kVision20Classes,sentry_obj_info_e.kLabel,i)==class20_label_e.kBus):
              print("object#%d: Bus, "%(i), end='')
            if (sengo2.GetValue(sengo2_vision_e.kVision20Classes,sentry_obj_info_e.kLabel,i)==class20_label_e.kCar):
              print("object#%d: Car, "%(i), end='')
            if (sengo2.GetValue(sengo2_vision_e.kVision20Classes,sentry_obj_info_e.kLabel,i)==class20_label_e.kCat):
              print("object#%d: Cat, "%(i), end='')
            if (sengo2.GetValue(sengo2_vision_e.kVision20Classes,sentry_obj_info_e.kLabel,i)==class20_label_e.kChair):
              print("object#%d: Chair, "%(i), end='')
            if (sengo2.GetValue(sengo2_vision_e.kVision20Classes,sentry_obj_info_e.kLabel,i)==class20_label_e.kCow):
              print("object#%d: Cow, "%(i), end='')
            if ((sengo2.GetValue(sengo2_vision_e.kVision20Classes,sentry_obj_info_e.kLabel,i)) == 11):
              print("object#%d: DiningTable, "%(i), end='')
            if ((sengo2.GetValue(sengo2_vision_e.kVision20Classes,sentry_obj_info_e.kLabel,i)) == 12):
              print("object#%d: Dog, "%(i), end='')
            if ((sengo2.GetValue(sengo2_vision_e.kVision20Classes,sentry_obj_info_e.kLabel,i)) == 13):
              print("object#%d: Horse, "%(i), end='')
            if ((sengo2.GetValue(sengo2_vision_e.kVision20Classes,sentry_obj_info_e.kLabel,i)) == 14):
              print("object#%d: Motorbike, "%(i), end='')
            if ((sengo2.GetValue(sengo2_vision_e.kVision20Classes,sentry_obj_info_e.kLabel,i)) == 15):
              print("object#%d: Person, "%(i), end='')
            if ((sengo2.GetValue(sengo2_vision_e.kVision20Classes,sentry_obj_info_e.kLabel,i)) == 16):
              print("object#%d: PottedPlant, "%(i), end='')
            if ((sengo2.GetValue(sengo2_vision_e.kVision20Classes,sentry_obj_info_e.kLabel,i)) == 17):
              print("object#%d: Sheep, "%(i), end='')
            if ((sengo2.GetValue(sengo2_vision_e.kVision20Classes,sentry_obj_info_e.kLabel,i)) == 18):
              print("object#%d: Sofa, "%(i), end='')
            if ((sengo2.GetValue(sengo2_vision_e.kVision20Classes,sentry_obj_info_e.kLabel,i)) == 19):
              print("object#%d: Train, "%(i), end='')
            if ((sengo2.GetValue(sengo2_vision_e.kVision20Classes,sentry_obj_info_e.kLabel,i)) == 20):
              print("object#%d: Tvmonitor, "%(i), end='')
              
            x = sengo2.GetValue(sengo2_vision_e.kVision20Classes, sentry_obj_info_e.kXValue, i)
            y = sengo2.GetValue(sengo2_vision_e.kVision20Classes, sentry_obj_info_e.kYValue, i)
            w = sengo2.GetValue(sengo2_vision_e.kVision20Classes, sentry_obj_info_e.kWidthValue, i)
            h = sengo2.GetValue(sengo2_vision_e.kVision20Classes, sentry_obj_info_e.kHeightValue, i)
            print("x=%d, y=%d, w=%d, h=%d"%(x, y, w, h))
            time.sleep(0.2)
            print("\n")
