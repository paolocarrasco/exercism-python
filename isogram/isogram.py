import re

def is_isogram(string):

    characters = {}
    isIsogram = True

    for c in re.sub(r'[\s-]', "", string.lower()):

        if c in characters:
            isIsogram = False
            break
        else:
            characters[c] = 1

    return isIsogram
