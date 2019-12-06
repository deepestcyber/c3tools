#!/bin/bash
for i in {1..255}; do
	# 35c3
	#curl "https://guru3.eventphone.de/event.rb/phonebook?order=extension&page=$i" | egrep '[ ]{5}[0-9]+'
	# 36c3
	curl 'https://guru3.eventphone.de/event.exe/phonebook?order=extension&page='$i | egrep -o 'tel:[0-9]+' | sed -e 's/tel://'
done > phonebook.txt
