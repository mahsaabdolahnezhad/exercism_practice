'''this module determines whether a number is perfect , abundant or deficient '''


def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number <= 0:
        raise ValueError('Classification is only possible for positive integers.')

    sum_factor=0

    for num in range(1, number):
        if number%num==0:
            sum_factor = sum_factor + num


    if sum_factor == number:
        return 'perfect'
    if sum_factor > number:
        return 'abundant'
    if sum_factor < number:
        return 'deficient'
    
