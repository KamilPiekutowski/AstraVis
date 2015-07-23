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
    if line[3] == -1:
        line[3] == 0
    tree2.append([line[3], line[1]])

for line in tree2:
    key = line[1]
    tree3.append([int(line[0]),int(line[1])])


#del data[:]

#for elem in tree:
#    print elem.id


print "Creating json file.."

#outfile1 = open("tree.data","wb")
#outfile2 = open("hierarchy.data","wb")

#outfile1.write("[")
#for line in tree1[:1000]:
#    outfile1.write("%s,\n" % line)
#outfile1.write("%s\n" % tree1[1000])
#outfile1.write("]")

#for line in tree2[:1000]:
#    outfile2.write("%s\n" % line)

#for i in tree3:
#    print i





tree = []

single_nodes = []

tree3[0][0] = 0


def foo(key,node,isFirst):
    for i in tree3:
        if i[0] == key and i[1] != -1:
            new = {'name': "%s" % i[1], 'children': []}
            node.append(new)
            last = len(node)-1
#            print last
#            print node
            node.append(foo(i[1],node[last]['children'],0))
            #new.update({'name': "%s" % i[1],'children' : []})

            #print [0]

for i in single_nodes:
    print i
    #tree.append({'name': '%s' % i[0]})



#foo(0,tree,1)
for i in tree3:
    print i


#output = open('test.json','wb')
#json.dump(tree,output)
