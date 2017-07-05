def fancy_divide(list_of_numbers, index):
    denom = list_of_numbers[index]
    return [simple_divide(item, denom) for item in list_of_numbers]


def simple_divide(item, denom):
    """Divide item by denom.
    
    On a division by 0 error, the value 0 is returned.
    """
    
    try:
        result = item / denom
    except ZeroDivisionError:
        return 0
    else:
        return result
