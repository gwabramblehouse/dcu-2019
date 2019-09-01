#!/usr/bin/python3
from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.start_preview()
sleep(3)
camera.capture("test-image.jpg")
camera.stop_preview()
