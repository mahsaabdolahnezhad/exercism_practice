'''in this module we are trying to create a function to identify isogram words'''

from collections import Counter

def is_isogram(phrase):
    '''we are counting every letter except hyphen and spaces to determine isogram words.'''
    phrase_letter_count = Counter(phrase.lower().replace(" ", "").replace("-",""))
    letter_count = [letter for letter , count in phrase_letter_count.items() if count > 1]
    if not letter_count:
        return True
    return False

    
