#!/bin/bash

pattern_file=$1

bs=1000;
for i in $(seq 0 $bs $(wc -l $pattern_file | cut -d " " -f 1)); do
	head -n $(($i + $bs)) $pattern_file | tail -n $bs > "tmp_$i"
	#echo $i $(($i + $bs));
	egrep -f "tmp_$i" -i words
	rm "tmp_$i"
done
