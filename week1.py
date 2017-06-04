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


def problem3(s):
    """For a given string, print the longest substring in alphabetical order.
    
    Example, aejka will return "aejk".
    """
    
    best_start = 0
    best_end = 0
    curr_start = 0
    curr_end = 0
    
    while curr_end < len(s):
        
        if s[curr_end] < s[curr_end-1]:
            
            if curr_end - curr_start > best_end - best_start:
                best_end = curr_end
                best_start = curr_start
            
            curr_start = curr_end
        
        curr_end = curr_end + 1
    
    if curr_end - curr_start > best_end - best_start:
        best_end = curr_end
        best_start = curr_start
    
    print("Longest substring in alphabetical order is:", s[best_start:best_end])


def test_problem3():
    
    problem3("abc")
    print("expected: abc\n")
    
    problem3("abcz")
    print("expected: abcz\n")
    
    problem3("abcza")
    print("expected: abcz\n")
    
    problem3("yczrrglyquxrvvmmaav")
    print("expected: gly\n")
    
    problem3("lmjwcbzehoogsfmnymx")
    print("expected: ehoo\n")
