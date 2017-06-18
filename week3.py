# -*- coding: utf-8 -*-

def odd_tuples(t):
    """
    t: a tuple
    
    returns: tuple, every other element of t
    """
    
    o = ()
    i = 0
    while i < len(t):
        
        # concatenate tuples
        # splice is required here to convert element to tuple
        o = o + t[i:i+1]
        i += 2
        
    return o