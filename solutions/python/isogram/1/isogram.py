from collections import Counter
'''in this module we are trying to create a function to identify isogram words'''

def is_isogram(phrase):
    '''we are counting every letter except hyphen and spaces to determine isogram words.'''
    d = Counter(phrase.lower().replace(" ", "").replace("-",""))
    res = [c for c, count in d.items() if count > 1]
    if not res:
        return True
    return False

    
