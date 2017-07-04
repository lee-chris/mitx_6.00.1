# -*- coding: utf-8 -*-

def is_triangular(k):
    """
    k, a positive integer
    returns True if k is triangular and False if not
    """
    
    i = 1
    
    while k >= 0:
        
        k -= i
        i += 1
        
        if k == 0:
            return True
    
    return False
        
