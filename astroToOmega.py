#!/usr/bin/python

from yt.utilities.sdf import load_sdf

#fileToOpen = "ds14_scivis_0128/ds14_scivis_0128_e4_dt04_1.0000"
#fileToOpen = "ds14_scivis_0128/ds14_scivis_0128_e4_dt04_0.4700"


#-------------------------------------------------------------------------------
# CODE
import struct
from random import *
from math import *
import sys


if len(sys.argv) < 2:
   print "usage: %s <filename>" % sys.argv[0]
   quit()

print "data%s.xyzb" % sys.argv[1][-4:]

fileToOpen = sys.argv[1]
fileToSave = "data%s.xyzb" % sys.argv[1][-4:]

sdfdata = load_sdf(fileToOpen)
file = open(fileToSave, 'wb')

'''
for ix in range(0,sdfdata['x'].size):

    if (sdfdata['vx'][ix] > 0):
        maxVX = minVX = sdfdata['vx'][ix]
        print (ix)
        break

for iy in range(0,sdfdata['x'].size):
    
    if (sdfdata['vy'][iy] > 0):
        maxVY = minVY = sdfdata['vy'][iy]
        print (iy)
        break

for iz in range(0,sdfdata['x'].size):
    
    if (sdfdata['vz'][iz] > 0):
        maxVZ = minVZ = sdfdata['vz'][iz]
        print (iz)
        break
'''
maxVel = minVel = sqrt( (sdfdata['vx'][0] * sdfdata['vx'][0]) + (sdfdata['vy'][0] * sdfdata['vy'][0]) + (sdfdata['vz'][0] * sdfdata['vz'][0]) )

vel = 0.0

for v in range(0,sdfdata['x'].size):
    vel = sqrt( (sdfdata['vx'][v] * sdfdata['vx'][v]) + (sdfdata['vy'][v] * sdfdata['vy'][v]) + (sdfdata['vz'][v] * sdfdata['vz'][v]) )

    if vel > maxVel:
        maxVel = vel
    if vel < minVel:
        minVel = vel



'''
maxVY = sdfdata['vy'][0]
maxVZ = sdfdata['vz'][0]

minVY = sdfdata['vy'][0]
minVZ = sdfdata['vz'][0]
'''

old_minX = 0.0
old_maxX = 0.0
'''
old_minY = 0.0
old_maxY = 0.0

old_minZ = 0.0
old_maxZ = 0.0


xV = 0.0
yV = 0.0
zV = 0.0
'''

new_min = 0.1
new_max = 1.0

#print 'Available halo quantities:', sdfdata.keys()
print ("start")

'''
for i in range(0,sdfdata['x'].size):
    
    xV = abs(sdfdata['vx'][i])
    yV = abs(sdfdata['vy'][i])
    zV = abs(sdfdata['vz'][i])

    if xV > maxVX:
        maxVX = xV
    if yV > maxVY:
        maxVY = yV
    if zV > maxVZ:
        maxVZ = zV
    
    if xV < minVX:
        minVX = xV
    if yV < minVY:
        minVY = yV
    if zV < minVZ:
        minVZ = zV
'''

"""
    if (xV > 2550.4) or (xV < -2193.12):
        print "xV"
        print (xV)
    if (yV > 2722.93) or (yV < -2355.75):
        print "yV"
        print (yV)
    if (zV > 2257.95) or (zV < -2229.78):
        print "zV"
        print (zV)
"""


#old_valueX = sdfdata['vx'][i]

vel2 = 0.0

for s in range(0,sdfdata['x'].size):
    
    #xV = abs(sdfdata['vx'][s])
    #yV = abs(sdfdata['vy'][s])
    #zV = abs(sdfdata['vz'][s])
    
    vel2 = sqrt( (sdfdata['vx'][s] * sdfdata['vx'][s]) + (sdfdata['vy'][s] * sdfdata['vy'][s]) + (sdfdata['vz'][s] * sdfdata['vz'][s]) )

    old_minX = minVel
    old_maxX = maxVel

    new_valueX = ( (vel2 - old_minX) / (old_maxX - old_minX) ) * (new_max - new_min) + new_min
    
    if new_valueX > 1.0 or new_valueX < 0.0:
        print (new_valueX)

    file.write(struct.pack('ddddddd', sdfdata['x'][s], sdfdata['y'][s], sdfdata['z'][s], new_valueX, new_valueX, new_valueX, 1.0))

'''
    old_minY = minVY
    old_maxY = maxVY
    
    new_valueY = ( (yV - old_minY) / (old_maxY - old_minY) ) * (new_max - new_min) + new_min

    old_minZ = minVZ
    old_maxZ = maxVZ
    
    new_valueZ = ( (zV - old_minZ) / (old_maxZ - old_minZ) ) * (new_max - new_min) + new_min
'''


#print maxVX, maxVY, maxVZ
#print minVX, minVY, minVZ

print minVel, maxVel

file.close()


print("Finished: {0}".format(1))
