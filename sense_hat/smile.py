#coding:UTF-8
from sense_hat import SenseHat
import time

sense=SenseHat()
sense.set_rotation(90)
w=(255,255,255)
r=(255,0,0)

happy = [
w, w, w, w, w, w, w, w,
w, w, w, w, w, w, w, w,
w, w, r, w, w, r, w, w,
w, w, w, w, w, w, w, w,
w, w, w, w, w, w, w, w,
w, r, w, w, w, w, r, w,
w, w, r, r, r, r, w, w,
w, w, w, w, w, w, w, w
]

sad = [
w, w, w, w, w, w, w, w,
w, w, w, w, w, w, w, w,
w, w, r, w, w, r, w, w,
w, w, w, w, w, w, w, w,
w, w, w, w, w, w, w, w,
w, w, r, r, r, r, w, w,
w, r, w, w, w, w, r, w,
w, w, w, w, w, w, w, w
]
sense.set_pixels(happy) #设置矩阵像素值
while 1:
    time.sleep(1)
    x,y,z=sense.get_accelerometer_raw().values()
    while x<2 and y<2 and z<2:
        x,y,z=sense.get_accelerometer_raw().values()
    sense.set_pixels(sad)
    sense.low_light=True    #屏幕变亮或变暗

    time.sleep(1)
    x,y,z=sense.get_accelerometer_raw().values()
    while x<2 and y<2 and z<2:
        x,y,z=sense.get_accelerometer_raw().values()
    sense.set_pixels(happy)
    sense.low_light=False    #屏幕变亮或变暗
    
