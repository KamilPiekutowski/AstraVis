#!/usr/bin/python

import thingking as tk
import numpy as np
import json
from treeClass import HaloTree as tc
import sys
import os
from os.path import basename

if len(sys.argv) <= 1:
    print "usage: %s <file_path/name> [OPTION] -d for debugging" % sys.argv[0]
    exit(-1)

DEBUG = 0

if len(sys.argv) == 3 and sys.argv[2] == '-d':
    DEBUG = 1;

filei = sys.argv[1]
fileo = 'halos_JSON/' + basename(os.path.splitext(filei)[0]) + '.JSON'

if DEBUG:
    print basename(os.path.splitext(filei)[0]) + '.JSON'
    print "Reading file... %s" % filei



po= open(filei)

data = []

if DEBUG:
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

print len(data)

for line in data:
    if line[3] == -1:
        line[3] == 0
    tree2.append([line[3], line[1]])

for line in tree2:
    key = line[1]
    tree3.append([int(line[0]),int(line[1])])


#del data[:]

#for elem in tree:
#    print elem.id

if DEBUG:
    print "Creating json file.."


#for line in tree2[:1000]:
#    outfile2.write("%s\n" % line)

#for i in tree3:
#    print i





tree = []

single_nodes = []

tree3[0][0] = 0


def foo(key,node,isFirst):
    for i in tree3[:2]:
        if i[0] == key and i[1] != '-1':
            new = {'name': "%s" % i[1], 'children': []}
            node.append(new)
            last = len(node)-1
#            print last
#            print node
            node.append(foo(i[1],node[last]['children'],0))
            #new.update({'name': "%s" % i[1],'children' : []})

            #print [0]




foo(0,tree,1)


output = open(fileo,'wb')
if DEBUG:
    print "Creating file...%s" % fileo

json.dump(tree,output)

for line in tree3:
    print line
