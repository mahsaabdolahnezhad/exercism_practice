'''function to calculate score of dart'''


def score(x, y):
    '''we first calculate the distance from (0,0) point'''
    distance = (x**2 + y**2) **0.5

    if distance <= 1:
        return 10;
    elif distance <=5:
        return 5;
    elif distance <= 10:
        return 1;
    else:
        return 0;

    
