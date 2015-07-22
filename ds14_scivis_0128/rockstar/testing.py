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





tree = []


def foo(key,node):
    for i in data:
        if i[0]  == key:
            new = []
            new.append("%s" % i[1])
            node.append(new)
            #print [0]
            foo (i[1],node[len(node)-1])


def _build_structure(self, item):
    if item in tree:
        return item
    else:
        return [self._build_structure(child) for child in item.children]

def prettyprint(node,spacing):
    for i in node:
        if i[0] != '-1':
            sys.stdout.write('-%s' % i[0])
        prettyprint(i[1:],spacing+1)
        sys.stdout.write('\n')
        for x in range(0,spacing-1):
            sys.stdout.write(' |')
        sys.stdout.write('  ')

dictionary = {}

_build_structure(dictionary,tree)


foo(0,tree)
prettyprint(tree,0)
print json.dumps(tree)


output = open('test.json','wb')
json.dump(tree,output)
