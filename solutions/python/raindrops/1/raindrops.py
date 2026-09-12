'''convert a number into corresponding raindrop sound'''
def convert(number):
    '''a function to covert remainders to answers'''
    result = ""
    if number%3 == 0:
        result = result + "Pling"
    if number%5 == 0: 
        result = result + "Plang"
    if number%7 == 0:
        result = result + "Plong"
    if result == "":
        return str(number)
    return result