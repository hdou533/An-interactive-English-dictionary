import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(w):
    w = w.lower()
    if w in data:  # exactly the same
        return data[w]
    elif w.title() in data: # to match with proper nouns
        return data[w.title()]
    elif w.upper() in data: # such as 'USA'
        return data[w.upper()]

    elif get_close_matches(w, data.keys(), cutoff=0.8) != []:  # find similar words
        yesNo = input("Did you mean %s instead? Enter Y if yes, or N if no: " %get_close_matches(w, data.keys())[0]).lower()
        
        if yesNo == "y":
            return data[get_close_matches(w, data.keys())[0]]
        elif yesNo == 'n':
            return "The word doesn't exit, please double check it."
        else:
            return "We didn't understand your entry. "

    else:
        return "The word doesn't exit, please double check it."
        

word = input("Input a word: ")

output = translate(word)

if type(output) == list:

    for item in output:
        print(item)
else:
    print(output)

