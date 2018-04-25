import json

# Download phonebook via running
# curl 'https://eventphone.de/guru2/phonebook?event=34C3&format=json' > phonebook.json


with open('phonebook.json', 'r') as f: 
    d = json.load(f)


def find_synonym(s):
    a = {
        0: '0', 1: '1', 2: 'ABC', 
        3: 'DEF', 4: 'GHI', 5: 'JKL', 
        6: 'MNO', 7: 'PQRS', 8: 'TUV',
        9: 'WXYZ'
    }
    words = []
    for n in s:
        choices = a[int(n)]
        if len(words) == 0:
            words = list(choices)
        else:
            new_words = []
            for c in choices:
                new_words += [w + c for w in words]
            words = new_words
    return ",".join([w for w in words if len(w) == len(s)])


all_exts = set(range(2101, 8999))
taken_exts = {int(n['extension']) for n in d if n['extension'].isdigit()}

free_exts = all_exts.difference(taken_exts)

print("\n".join([str(n) +" __ " + find_synonym(str(n)) for n in sorted(free_exts)]))
