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
        

def print_without_vowels(s):
    '''
    s: the string to convert
    Finds a version of s without vowels and whose characters appear in the 
    same order they appear in s. Prints this version of s.
    Does not return anything
    '''
    
    out = ""
    vowels = "aeiou"
    
    for c in s:
        if not c in vowels:
            out += c
    
    print(out)
