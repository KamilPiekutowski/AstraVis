#!/usr/bin/python

import sys
from yt.utilities.sdf import load_sdf
import struct
from random import *
from math import *


print sys.argv[1]

fileToOpen = sys.argv[1]
fileToSave = sys.argv[1] + ".adf"

sdfdata = load_sdf(fileToOpen)

file = open(fileToSave, 'wb')
#-------------------------------------------------------------------------------
# CODE



print 'Available halo quantities:', sdfdata.keys()

for i in range(0,sdfdata['x'].size):

    #print("Done with: {0}".format(i))
    file.write(struct.pack('ddddddd', sdfdata['x'][i], sdfdata['y'][i], sdfdata['z'][i], 1.0, 1.0, 1.0, 1.0))
#print i, sdfdata['x'][i], sdfdata['z'][i], sdfdata['y'][i]


file.close()


print("Finished: {0}".format(1))
