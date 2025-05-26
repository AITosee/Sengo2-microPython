import time
from Sengo2 import *
from mpython import *
from machine import UART


uart1 = UART(1, baudrate=57600, tx=Pin.P14, rx=Pin.P13)

sengo2 = Sengo2(0x60)

# 自定义函数
def UART():
  global my_variable, key_A, key_B, param_set, id, num, key_H, key_Y, key_N, i
  sengo2.begin(uart1)
def Param_Set():
  global my_variable, key_A, key_B, param_set, id, num, key_H, key_Y, key_N, i
  if (param_set == 1):
    param_set = 0
    Button_A()
    Button_B()
    oled.fill_rect(48,48,16,16,0)
    oled.show()
    time.sleep(0.2)
    oled.DispChar((str(id)), 48, 48, 1)
    oled.DispChar("Operation Done", 0, (2-1)*16, 1)
    oled.show()
    time.sleep(0.2)
    oled.fill_rect(0, (2-1)*16, 128, 16, 0)
    oled.show()
def Result_Display():
  global my_variable, key_A, key_B, param_set, id, num, key_H, key_Y, key_N, i
  if (param_set == 0):
    # Sengo2不主动返回检测识别结果，需要主控板发送指令进行读取。读取的流程：首先读取识别结果的数量，接收到指令后，Sengo2会刷新结果数据，如果结果数量不为零，那么主控再发送指令读取结果的相关信息。请务必按此流程构建程序。
    num = (sengo2.GetValue(sengo2_vision_e.kVisionLearning, sentry_obj_info_e.kStatus))
    i = 1
    for index in range(num):
      # 深度学习算法返回的xywh四个值均为固定值，无实际意义。
      oled.DispChar((str("Object: ") + str((sengo2.GetValue(sengo2_vision_e.kVisionLearning,sentry_obj_info_e.kLabel,i)))), 0, (2-1)*16, 1)
      oled.show()
      time.sleep(0.2)
      oled.fill_rect(0, (2-1)*16, 128, 16, 0)
      oled.fill_rect(0, (3-1)*16, 128, 16, 0)
      oled.show()
      time.sleep(0.2)
      i = (i + 1)
def I2C():
  global my_variable, key_A, key_B, param_set, id, num, key_H, key_Y, key_N, i
  sengo2.begin(i2c)
def Button_A():
  global my_variable, key_A, key_B, param_set, id, num, key_H, key_Y, key_N, i
  if (key_A == 1):
    key_A = 0
    oled.DispChar("Point  at the object", 0, (2-1)*16, 1)
    oled.show()
    num = 3
    for index in range(3):
      oled.DispChar((str(num)), 0, (3-1)*16, 1)
      oled.show()
      time.sleep(1)
      num = (num - 1)
    oled.fill_rect(0, (2-1)*16, 128, 16, 0)
    oled.fill_rect(0, (3-1)*16, 128, 16, 0)
    oled.show()
    time.sleep(0.2)
    oled.DispChar("Saving...", 0, (2-1)*16, 1)
    sengo2.SetParam(sengo2_vision_e.kVisionLearning,[0, 0,0, 0, 100], id);
    time.sleep(2)
    id = (id + 1)
    if (id > 15):
      id = 1
def Button_B():
  global my_variable, key_A, key_B, param_set, id, num, key_H, key_Y, key_N, i
  if (key_B == 1):
    key_B = 0
    id = (id - 1)
    if (1 > id):
      id = 15
    sengo2.SetParam(sengo2_vision_e.kVisionLearning,[0, 0,0, 0, 0], id);
    time.sleep(2)

# 事件回调函数
def on_button_a_down(_):
  time.sleep_ms(10)
  if button_a.value() == 1: return
  global param_set
  global key_A
  param_set = 1
  key_A = 1
def on_button_b_down(_):
  time.sleep_ms(10)
  if button_b.value() == 1: return
  global param_set
  global key_B
  param_set = 1
  key_B = 1


button_a.irq(trigger=Pin.IRQ_FALLING, handler=on_button_a_down)
button_b.irq(trigger=Pin.IRQ_FALLING, handler=on_button_b_down)
param_set = 0
key_A = 0
key_B = 0
num = 0
id = 1
i = 0
# 等待Sengo2初始化完毕，此延时不可去掉
time.sleep(2)
I2C()
sengo2.VisionBegin(sengo2_vision_e.kVisionLearning)
oled.DispChar("Algo: Learning", 0, 0, 1)
oled.DispChar("Index=", 0, 48, 1)
oled.DispChar((str(id)), 48, 48, 1)
oled.show()
while True:
  Param_Set()
  Result_Display()
