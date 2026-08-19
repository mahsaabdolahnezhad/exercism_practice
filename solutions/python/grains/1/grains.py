'''count the number of grains the servent will gain'''

def square(number):
    '''each square follows the pattern of 2^(number-1)'''
    if number <= 0 or number > 64:
        raise ValueError("square must be between 1 and 64")
    return 2**(number-1)


def total():
    '''the total is  power of 2 by the number of chess suqares minus 1'''
    return (2**64)-1