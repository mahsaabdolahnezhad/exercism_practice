'''a programmer to design anwsers from a lackadasical character'''

def response(hey_bob):
    '''this function uses conditional terms to create desired answers'''
    if hey_bob == "" or hey_bob.isspace():
        return "Fine. Be that way!"
    elif hey_bob.strip()[-1] == "?"and hey_bob.isupper():
        return "Calm down, I know what I'm doing!"
    elif hey_bob.isupper():
        return "Whoa, chill out!"
    elif hey_bob.strip()[-1] == "?":
        return "Sure."
    return "Whatever."