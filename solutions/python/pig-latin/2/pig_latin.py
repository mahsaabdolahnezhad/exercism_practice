'''using rules to create piglatin language'''

def translate(words):
    '''function to creae piglatin'''
    texts = words.split()
    result = []
    for text in texts:
        position = text.find("qu")
        position1= text.find("y")
        position2 = -1
        for index , char in enumerate(text):
            if char in "aeiou":
                position2 = index
                break
        has_vowel = False
        for char in text[:position1]:
            if char in "aeiou":
                has_vowel = True
                break 
            
        if text[0].lower() in "aeiou" or text[:2].lower() == "xr" or text[:2].lower()== "yt":
            result.append(text + "ay")
        elif position != -1 and position < position2:
            result.append(text[position+2:] + text[:position+2] +"ay")
        elif position1 != -1 and not has_vowel and position1 > 0:
            result.append(text[position1:] + text[:position1] + "ay")
        else:
            result.append(text[position2:] + text[:position2] + "ay")
    return " ".join(result)
            
