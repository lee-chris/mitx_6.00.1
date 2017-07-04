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
        if not c.lower() in vowels:
            out += c
    
    print(out)


def largest_odd_times(L):
    """ Assumes L is a non-empty list of ints
        Returns the largest element of L that occurs an odd number 
        of times in L. If no such element exists, returns None """
    
    dist = {}
    
    for n in L:
        
        if not n in dist:
            dist[n] = 1
        else:
            dist[n] += 1
            
    max_key = None
    
    for key in dist:
        
        # if odd
        if not dist[key] % 2 == 0:
            if max_key == None or key > max_key:
                max_key = key
    
    return max_key


def dict_invert(d):
    '''
    d: dict
    Returns an inverted dictionary according to the instructions above
    '''
    
    inverse = {}
    
    for key in d:
        
        val = d[key]
        
        if not val in inverse:
            inverse[val] = []
        
        if not key in inverse[val]:
            inverse[val].append(key)
            inverse[val].sort()
    
    return inverse


def general_poly (L):
    """ L, a list of numbers (n0, n1, n2, ... nk)
    Returns a function, which when applied to a value x, returns the value 
    n0 * x^k + n1 * x^(k-1) + ... nk * x^0 """
    
    def fn(x):
        
        val = 0
        k = len(L) - 1
        
        for i in L:
            val += i * x ** k
            k = k - 1
        
        return val
            
    return fn


def is_list_permutation(L1, L2):
    '''
    L1 and L2: lists containing integers and strings
    Returns False if L1 and L2 are not permutations of each other. 
            If they are permutations of each other, returns a 
            tuple of 3 items in this order: 
            the element occurring most, how many times it occurs, and its type
    '''
    
    def get_distribution(L):
        
        dist = {}
        for i in L:
            
            if not i in dist:
                dist[i] = 1
            else:
                dist[i] += 1
        
        return dist
        
    for i in L1:
        if not i in L2:
            return False
    
    for i in L2:
        if not i in L1:
            return False
    
    dist = get_distribution(L1)
    
    max_count = 0
    max_key = None
    
    for key in dist:
        
        count = dist[key]
        if count > max_count:
            max_count = count
            max_key = key

    if max_key == None:
        return (None, None, None)
    
    return (max_key, max_count, type(max_key))