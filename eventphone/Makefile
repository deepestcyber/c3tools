phonebook.txt:
	./fetch_phonebook.sh > phonebook.txt

free_numbers: phonebook.txt
	python find_free_numbers.py > free_numbers

free_word_patterns: free_numbers
	sed -e 's/[0-9]* __ //' free_numbers | tr ',' '\n' | sed -e 's/^/\\</' -e 's/$$/\\>/'  > free_word_patterns

find_free_words: free_word_patterns
	./find_free_words.sh free_word_patterns
