'''in this module we are trying to create a function to identify isogram words'''

from collections import Counter

def is_isogram(phrase):
    '''we are counting every letter except hyphen and spaces to determine isogram words.'''
    phraseLetterCount = Counter(phrase.lower().replace(" ", "").replace("-",""))
    letterCount = [letter for letter , count in phraseLetterCount.items() if count > 1]
    if not letterCount:
        return True
    return False

    
