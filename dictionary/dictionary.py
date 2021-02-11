import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def meaning(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif w.title in data:
        return data[w.title()]
    elif w.upper in data:
        return data[w.upper()]        
    elif len(get_close_matches(w,data.keys())) > 0:
        yn = input("Do you mean %s instead? Enter y if yes else enter n: " % get_close_matches(w, data.keys()) [0])
        if yn == 'y' or 'Y':
             return data[get_close_matches(w, data.keys())[0]]
        else:
            return "Word not found"
    else:
        return "Word not found."    

word = input("Enter word: ")    
output = (meaning(word))

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)