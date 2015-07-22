#!/bin/bash
if [ ! -f ./trees/tree_0_0_0.dat ]
then
	"Cannot locate ./trees/tree_0_0_0.dat!"
	"Downloading ./trees/tree_0_0_0.dat!"
	mkdir trees
	wget -O ./trees/tree_0_0_0.dat https://www.dropbox.com/s/hbxc3ir43wmfei7/tree_0_0_0.dat?dl=0
fi

mkdir halos halos_JSON

./halos2files.sh

TOTAL=0;
for f in halos/*
do
	TOTAL=$((TOTAL+1))
done
printf "Creating JSON files...\n"
COUNT=0 ;
for f in halos/*
do
	NAME=./halos_JSON/$(basename ${f%.*}".json") 
	./tree.py $f > $NAME
	PROG=$(bc <<< "scale=2;$COUNT/$TOTAL*100")
	printf "\rProgress [%s%%]: %s to: %s" ${PROG%.*} $f $NAME
	COUNT=$((COUNT+1))
done
printf "\rProgress 100%%\n" $PROG
