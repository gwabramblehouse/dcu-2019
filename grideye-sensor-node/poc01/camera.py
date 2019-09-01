#!/usr/bin/python3

from picamera import PiCamera
from time import sleep

camera = PiCamera()
#camera.resolution = (2592, 1944)
#camera.resolution = (260,106)
#camera.vflip = True
#camera.hflip = True

#camera.start_preview()
camera.start_preview(fullscreen=False,window=(1,70, 240,240))
#camera.start_preview(fullscreen=False,window=(1,70, 128, 128))
sleep(3600*12)
#for i in range(10):
#    sleep(0.1)
#    camera.capture("/home/pi/Desktop/test-image-no-preview" + str(i) + ".jpg")
camera.stop_preview()
