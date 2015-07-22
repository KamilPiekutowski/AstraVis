#!/bin/bash

./treeparse.py ../trees/tree_0_0_0.dat

cat tree.data | sed 's/\\//g' > tree.data_

mv tree.data_ tree.data
