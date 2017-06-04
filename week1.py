# -*- coding: utf-8 -*-
"""
Created on Sat Jun  3 18:53:08 2017

@author: Chris Lee
"""

def problem1(s):
    """For a given string, print the number of vowels."""
    
    num_vowels = 0
    
    for c in s:
        
        if c == "a" or c == "e" or c == "i" or c == "o" or c == "u":
            num_vowels += 1
    
    print("Number of vowels:", num_vowels)


def problem2(s):
    """For a given string, print the number of times that 'bob' occurs."""
    
    num_bob = 0
    
    for i in range(len(s)):
        
        if s[i] == "b":
            if s[i:i+3] == "bob":
                num_bob += 1
    
    print("Number of times bob occurs is:", num_bob)