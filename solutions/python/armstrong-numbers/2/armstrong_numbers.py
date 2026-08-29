'''to caculate Armstrong number we have to power each digit to the number of digits'''
def is_armstrong_number(number):
    '''determine a number is Armstrong or not'''
    length = len(str(number))
    number_digits = str(number)
    final_num = 0
    for digit in number_digits:
        armstrong = int(digit)**length
        final_num = final_num + armstrong
        
        
    if final_num == number:
        return True
    return False
