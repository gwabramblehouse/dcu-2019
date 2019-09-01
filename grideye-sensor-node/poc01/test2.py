#!/usr/bin/python3
import time
import busio
import board
import adafruit_amg88xx
import socket

hostname=socket.gethostname()
i2c = busio.I2C(board.SCL, board.SDA)
amg = adafruit_amg88xx.AMG88XX(i2c)
n=0
while True:
    ticks = time.time()
    localtime = time.localtime(ticks)
    max_pixel=0
    s=""
    for row in amg.pixels:
        for pixel in row:
            if pixel > max_pixel:
                max_pixel = pixel
            s+=str('{0:.1f}'.format(pixel))
            s+= " "
        s+="\n"
    if n > 0:
        print('{0:4}-{1:02}-{2:02} {3:02}:{4:02}:{5:02} {6:.0f} {7:.1f} {8}\n{9}'.format(localtime[0], localtime[1], localtime[2], localtime[3], localtime[4], localtime[5], ticks, max_pixel, hostname, s))
    n += 1
    time.sleep(1)

