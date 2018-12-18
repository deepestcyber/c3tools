
a = {
        0: '0', 1: '1', 2: 'ABC',
        3: 'DEF', 4: 'GHI', 5: 'JKL',
        6: 'MNO', 7: 'PQRS', 8: 'TUV',
        9: 'WXYZ'
    }

z = {}

for k, v in a.items():
    for letter in v:
        z[letter.lower()] = k

import sys
for letter in sys.argv[1]:
    print(z[letter.lower()])
