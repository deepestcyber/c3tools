fetch_phonebook:
	curl https://micropoc.de/phonebook > phonebook.html
	(echo '['; egrep -o '^[ ]*[0-9][0-9]*$$' phonebook.html | while read n; do echo "{\"extension\": \"$$n\"},"; done; echo '{"extension": ""}]') > phonebook.json

free_numbers: fetch_phonebook
	python find_free_numbers.py > free_numbers

free_word_patterns: free_numbers
	sed -e 's/[0-9]* __ //' free_numbers | tr ',' '\n' | sed -e 's/^/\\</' -e 's/$$/\\>/'  > free_word_patterns

find_free_words: free_word_patterns
	for i in `seq 1 $$(expr $$(wc -l free_word_patterns | cut -d " " -f 1) / 1000)`; do (tail -n +$$(expr $$i \* 1000) free_word_patterns | head -n 1000 | egrep -f - -i words) ; done
