#!/usr/bin/python3
#############################################################################
# Home Mobility Monitor
#
#############################################################################

import argparse
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np
font = {'family' : 'normal',
        'size'   : 18}
plt.rc('font', **font)

def func(x, a, b, c):
    return a * np.exp(-b * x) + c

parser = argparse.ArgumentParser(description='Generate chart from CSV file')
parser.add_argument('-c', '--column', help = 'Data column of CSV data file', default=3, type = int)
parser.add_argument('-i', '--data_file', help = 'Name of CSV data file', type = str)
parser.add_argument('-o', '--image_file', help = 'Name of image file to create', type = str)
parser.add_argument('-l', '--legend',default = "Degrees Celsius",  help = 'Chart legend', type = str)
parser.add_argument('-t', '--title', help = 'Chart title', type = str)
args = parser.parse_args()
x = np.genfromtxt(args.data_file, delimiter=",", usecols=(0))
standing = np.genfromtxt(args.data_file, delimiter=",", usecols=(1))
sitting = np.genfromtxt(args.data_file, delimiter=",", usecols=(2))
prone = np.genfromtxt(args.data_file, delimiter=",", usecols=(3))
#x, y = a[1], a[0]
#plt.xlim(x.min() * 0.8, x.max()*1.1)
# plt.ylim(y.min() * 0.8, y.max()*1.1)
fig = plt.figure()
ax = fig.gca()
#ax.set_xticks(np.arange(x))
#ax.set_yticks(numpy.arange(0, 1., 0.1))
plt.grid()
plt.xlabel('Sensor height above subject (Metres)')
plt.plot(x, standing, label='Standing')
plt.plot(x, sitting, label='Sitting')
plt.plot(x, prone, label='Prone')
plt.ylabel("Area (Square Metres)")
plt.legend(loc='best')
#plt.scatter(x, y)
#plt.tight_layout()
plt.gcf().subplots_adjust(bottom=0.15)
#popt, pcov = curve_fit(func, x, y, maxfev=5000)
#plt.plot(x, func(x, *popt), 'r-')
#cb = plt.colorbar()
#cb.set_label(args.legend)
plt.suptitle("Coverage area for various poses")
#plt.show()
fig.savefig(args.image_file)
