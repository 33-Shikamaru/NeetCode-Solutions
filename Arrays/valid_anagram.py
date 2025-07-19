from collections import Counter

'''
Problem: Valid Anagram
-------

Given two strings `s` and `t`, return `true` if the two strings
are anagrams of each other, otherwise return `false`.

An anagram is a string that contains the exact same characters as
another string, but the order of the characters can be different.

-------
URL: https://neetcode.io/problems/is-anagram?list=neetcode150
'''

def valid_anagram(s: str, t: str) -> bool:
    # Creates dict-like structure in the form of a Counter (which is a subclass of a dict)
    # and compares the two Counter contents with each other.
    
    if len(s) != len(t):
        return False
    
    s_counts = Counter(s)
    t_counts = Counter(t)
    return s_counts == t_counts
    
def test1(s: str = 'racecar', t: str = 'carrace'):
    print('Test 1: PASSED' if valid_anagram(s, t) else 'Test 1: FAILED')
    
def test2(s: str = 'jar', t: str ='jam'):
    print('Test 2: PASSED' if not valid_anagram(s, t) else 'Test 2: FAILED')
    
test1()
test2()