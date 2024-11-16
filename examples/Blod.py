from mpython import *
from Sengo2 import *

sentry = Sengo2(0x61)


sentry.begin(i2c)
sentry.VisionBegin(sengo2_vision_e.kVisionBlob)
sentry.SetParamNum(sengo2_vision_e.kVisionBlob, 1)
sentry.SetParam(sengo2_vision_e.kVisionBlob, [0, 0, 15, 15, color_label_e.kColorGreen], 1)
while True:
    count = sentry.GetValue(sengo2_vision_e.kVisionBlob, sentry_obj_info_e.kStatus)
    i = 1
    for count in range(int(count)):
        print("{} {} {} {} {} {}".format(i, sentry.GetValue(sengo2_vision_e.kVisionBlob, sentry_obj_info_e.kXValue, i), sentry.GetValue(sengo2_vision_e.kVisionBlob, sentry_obj_info_e.kYValue, i), sentry.GetValue(sengo2_vision_e.kVisionBlob, sentry_obj_info_e.kWidthValue, i), sentry.GetValue(sengo2_vision_e.kVisionBlob, sentry_obj_info_e.kHeightValue, i), sentry.GetValue(sengo2_vision_e.kVisionBlob, sentry_obj_info_e.kLabel, i)))
        i = i + 1
