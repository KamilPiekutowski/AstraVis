#!/usr/bin/python

import thingking as tk
import numpy as np
import json
import os
from treeClass import HaloTree as tc

class node(object):
    def __init__(self, value, children = []):
        self.value = value
        self.children = children



print "reading file..."

po= open("trees/tree_0_0_0.dat")

data = []

print "parsing data..."
count = 0

output = open("tmp","wb")

for line in po:
    if not line[0] == '#':
        sp = (line.split())
	if len(sp) > 1:
		if sp[3] == '-1':
			count += 1
			output.close()
			print "Count: %s" % count
			print "Halo_ID: %s" % sp[1]
			output = open("halos/halo_%s.data" % sp[1],"wb")
	output.write(line)
if os.path.exists("tmp"):
	    os.remove("tmp")
