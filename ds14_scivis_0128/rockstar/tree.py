#!/usr/bin/python
import sys
import json

if len(sys.argv) < 2:
    print "usage: %s <filename.data<" % sys.argv[0]
    exit()

infile = open(sys.argv[1])

#data = [[0,1],
#        [1,2],
#        [1,3],
#        [1,4],
#        [2,5],
#        [2,6],
#        [3,7],
#        [4,8],
#        [4,9],
#        [5,10],
#        [5,11],
#        [5,12],
#        [6,13],
#        [6,14],
#        [7,-1],
#        [8,-1],
#        [9,-1],
#        [10,-1],
#        [11,-1],
#        [12,-1],
#        [13,-1],
#        [14,-1]]


#data = [[0,1],
#        [1,2],
#        [1,3],
#        [2,-1],
#        [3,-1]]

#data = [[0,1],
#        [1,2],
#        [2,3],
#        [3,-1]]

file_data = []
data = []

for i in infile:
    file_data.append(i.split())


for i in file_data:
    if i[3] == -1:
        i[3] = 0
    data.append([int(i[3]),int(i[1])])

data[0][0] = 0

for i in data:
    print i

#exit()

tree = []

single_nodes = []


keys = {}

for i in data:
    keys.update({i[1]:0})


children_count = {}

for i in data:
    if not children_count.get(i[0]):
        children_count.update({ i[0] : i[1]})

last_child = {}

for i in data:
    last_child.update({ i[0] : i[1]})



def foo(key,index,parent):
    for i in data[index:]:
        if i[0] == key:
            #print "first child is:%s" % children_count[key] + "key is:%s" % i[1]
            if children_count[key] == i[1]:
                print " "*index + "{"
            if key != 0:
                if keys[key] == 0:
                    keytxt = '"%s"' % key
                    keys[key] = 1;
                    text1 = '"name": "%s",' % i[0]
                    print " "*(index+2) + text1
                    if i[1] != -1:
                        text1 = '"parent": "%s",' % parent
                        text2 = '"children": ['
                        print " "*(index+2) + text1
                        print " "*(index+2) + text2
                    else:
                        text1 = '"parent": "%s"' % parent
                        print " "*(index+2) + text1
            else:
                    keytxt = "%s" % key
                    keys[key] = 1;
                    text1 = '"name": "%s",' % i[0]
                    print " "*(index+2) + text1
                    if i[1] != -1:
                        text1 = '"parent": "%s",' % parent
                        text2 = '"children": ['
                        print " "*(index+2) + text1
                        print " "*(index+2) + text2
                    else:
                        text1 = '"parent": "%s"' % parent
                        print " "*(index+2) + text1

            nextKey = 0
            if i[1] != -1:
                nextKey = i[1]
            foo(nextKey,index+1,i[0])
            if last_child[key] == i[1]:
                 if i[1] != -1:
                     print " "*(index) + "]"
                 print " "*(index) + "}"
            else:
                 print " "*(index) + "  ,"

        #elif i[1] == -1:
        #    print "Found: %s" % i

            

for i in single_nodes:
    print i
    #tree.append({'name': '%s' % i[0]})


foo(0,0,-1)

#for i in children_count:
#    print i
#print children_count
#print last_child
#print keys
#output = open('test.json','wb')
#json.dump(tree,output)
