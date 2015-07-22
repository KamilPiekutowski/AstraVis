#!/usr/bin/python

import thingking as tk
import numpy as np
import json
from treeClass import HaloTree as tc

class node(object):
    def __init__(self, value, children = []):
        self.value = value
        self.children = children



print "reading file..."

po= open("trees/tree_0_0_0.dat")

data = []

print "parsing data..."

for line in po:
    if not line[0] == '#':
        data.append(line.split())

data.pop(0)

tree1 = []
tree2 = []
tree3 = []

parent =  []
child = []


for line in data:
    tree1.append(json.dumps({ 'id': line[1], 'child': line[3],'position': {'x': line[17],'y': line[18],'z': line[19]}}))


for line in data:
    tree2.append([line[3],line[1],line[31]])
for elem in tree2:
    print elem
