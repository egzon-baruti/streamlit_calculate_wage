def calculate_wage(hours:float, rate:float):
    
    '''
    This function calculates wage base on two arguments hours and rate.
    Hours and rate must be float.
    Return float or None (if hours are in not acceptable range)
    '''

    if hours < 5 or hours > 60:
        # raise ValueError('The hours are more or less than 60 and 5 respectively')
        return None
    
    elif hours <= 40:
        wage = hours * rate
        return wage

    else:
        wage = (hours - 40) * (rate * 1.5) + 40 * rate
        return wage