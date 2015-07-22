#!/bin/bash

TOTAL=0;
for f in halos/*
do
	TOTAL=$((TOTAL+1))
done
printf "Creating JSON files...\n"
COUNT=0 ;
for f in halos/*
do
	./halosParse.py $f 
	PROG=$(bc <<< "scale=2;$COUNT/$TOTAL*100")
	printf "\rProgress [%s%%]: %s" ${PROG%.*} $f
	COUNT=$((COUNT+1))
done
printf "\rProgress 100%%\n" $PROG
rm tmp
printf "Cleaning up JSON files...\n"
COUNT=0 ;
for f in halos_JSON/*
do
	./remove_null.sh $f > tmp
	cp tmp $f
	PROG=$(bc <<< "scale=2;$COUNT/$TOTAL*100")
	printf "\rProgress [%s%%]: %s" ${PROG%.*} $f
	COUNT=$((COUNT+1))
done
printf "\rProgress 100%%\n" $PROG
rm tmp
