#!/bin/bash

pattern_file=$1

bs=10000;
for i in $(seq 0 $bs $(wc -l words | cut -d " " -f 1)); do
	head -n $(($i + $bs)) $pattern_file | tail -n $bs > tmp;
	#echo $i $(($i + $bs));
	egrep -f tmp -i words;
done
