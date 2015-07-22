#!/bin/bash

if [ $# -eq 0 ]
then
	echo "usage: $0 <input_file>"
	exit
fi

cat $1 | sed 's/, null//g' 

