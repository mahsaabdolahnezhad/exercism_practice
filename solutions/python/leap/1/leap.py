'''a fuction to calculate a leap year'''

def leap_year(year):
    '''the year should be divisible by 400 and 4 but not by 100 or other numbers to be a leap year'''
    return year%400 ==0 or year%4 ==0  and not year%100 ==0 
