from mpython import *
from Sengo2 import *

sentry = Sentry2(0x61)


sentry.begin(i2c)
sentry.VisionBegin(sengo2_vision_e.kVisionColor)
sentry.SetParamNum(sengo2_vision_e.kVisionColor, 1)
sentry.SetParam(sengo2_vision_e.kVisionColor, [120, 120, 40, 40, 0], 1)
while True:
    count = sentry.GetValue(sengo2_vision_e.kVisionColor, sentry_obj_info_e.kStatus)
    i = 1
    for count in range(int(count)):
        print("{} {} {} {} {}".format(i, sentry.GetValue(sengo2_vision_e.kVisionColor, sentry_obj_info_e.kRValue, 1), sentry.GetValue(sengo2_vision_e.kVisionColor, sentry_obj_info_e.kGValue, 1), sentry.GetValue(sengo2_vision_e.kVisionColor, sentry_obj_info_e.kBValue, 1), sentry.GetValue(sengo2_vision_e.kVisionColor, sentry_obj_info_e.kLabel, 1)))
        i = i + 1
