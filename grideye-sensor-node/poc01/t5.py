#!/usr/bin/python3
import time
import busio
import board
import adafruit_amg88xx
import numpy as np
i2c = busio.I2C(board.SCL, board.SDA)
amg = adafruit_amg88xx.AMG88XX(i2c)
n=0
sum=0
while True:
    tmax=0
    i = 0
    a = np.zeros(shape=(64))
    for row in amg.pixels:
        s=""
        for temp in row:
            a[i] = temp
            if temp > tmax:
                tmax = temp
            s+=str('{0:.0f}'.format(temp))
            s+= " "
            i+=1
#        print(s+"\n")
    time.sleep(1)
    n = n + 1
    percentile95 = np.percentile(a, 95)

    if n % 5:
        sum += tmax
        print( '{0:.0f} ({1:0.1f}) '.format(tmax, percentile95), end='')
    else:
        sum += tmax
        # print( '{0:.0f}'.format(sum)+ " ", end='')
        t = sum / 5
        print( '{0:.1f} '.format(t))
        sum = 0
        n = 0
