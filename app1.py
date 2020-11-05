############ imports

import json
from difflib import get_close_matches

############ data

data = json.load(open('dicio_proj/data.json'))

############ functions

def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif w.title() in data:
        return data [w.title()]
    elif w.upper() in data:
        return data[w.upper()]
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input('Did you mean %s instead? Y for yes N for no: ' % get_close_matches(w, data.keys())[0])
        if yn == 'Y' or 'y':
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == 'N' or 'n':
            return 'This word does not exist. Please double check it.'
        else:
            return "We didn't understand your entry."
    else:
        return 'This word does not exist. Please double check it.'

############ inputs
word = input('Enter word you wish to understand:')

output = translate(word)

if type(output) is list:
    for i in output:
        print (i)

else: 
    print (output)
