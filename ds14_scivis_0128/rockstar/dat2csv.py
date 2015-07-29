#!/usr/bin/python



print "reading file..."

po= open("trees/tree_0_0_0.dat")

data = []

print "parsing data..."


header = po.readline().split()

print header[4]



for line in po:
    if not line[0] == '#':
        data.append(line.split())

data.pop(0)

for i in data:
    print i[4]
