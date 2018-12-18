#!/bin/bash
for i in {1..126}; do
	curl "https://guru3.eventphone.de/event.rb/phonebook?order=extension&page=$i" | egrep '[ ]{5}[0-9]+'
done > phonebook.txt
