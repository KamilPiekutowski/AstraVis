#!/usr/bin/python
import sys
import json

data = [[0,1],
        [1,2],
        [1,3],
        [1,4],
        [2,5],
        [2,6],
        [3,7],
        [4,8],
        [4,9],
        [5,10],
        [5,11],
        [5,12],
        [6,13],
        [6,14],
        [7,-1],
        [8,-1],
        [9,-1],
        [10,-1],
        [11,-1],
        [12,-1],
        [13,-1],
        [14,-1],
        [15,-1],
        [16,-1],
        [17,-1]]


data = [[0,1],
        [1,2],
        [2,3],
        [3,4],
        [5,6],
        [6,7],
        [8,9]]

tree = []

single_nodes = []


def foo(key,node,isFirst):
    for i in data:
        if i[0] == key and i[0] != -1:
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



foo(0,tree,1)
print tree


output = open('test.json','wb')
json.dump(tree,output)
