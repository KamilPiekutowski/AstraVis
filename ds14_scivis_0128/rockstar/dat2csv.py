#!/usr/bin/python

import thingking as tk
import numpy as np
import json
from treeClass import HaloTree as tc


print "reading file..."

po= open("trees/tree_0_0_0.dat")

data = []

print "parsing data..."


print po.readline().split()


for line in po:
    if not line[0] == '#':
        data.append(line.split())

#for i in data:
#    print i
#data.pop(0)
