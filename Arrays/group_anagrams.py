from collections import defaultdict

'''
Problem: Group Anagrams
-------

Given an array of strings `strs`, group all anagrams together into sublists.
You may return the output in **any order**.

An **anagram** is a string that contains the exact same characters as 
another string, but the order of the characters can be different.

-------
URL: https://neetcode.io/problems/anagram-groups?list=neetcode150
'''

def groupAnagrams(strs: list[str]) -> list:
    # Create a table where we can insert similiar word structure
    # keys into the dict such that we would end up with a list of 
    # words appended to each key. Then return the list of all key values.
    
    sol = defaultdict(list)
    for word in strs:
        char_table = [0] * 26
        for char in word:
            char_table[ord(char) - ord('a')] += 1
        key = tuple(char_table)
        sol[key].append(word)
    return list(sol.values())


    
def test1(strs:list[str] = ["act","pots","tops","cat","stop","hat"]):
    sol = [["hat"], ["act", "cat"], ["pots", "tops", "stop"]]
    print('Test 1: PASSED' if sorted(groupAnagrams(strs)) == sorted(sol) else 'Test 1: FAILED')
    
def test2(strs:list[str] = ['x']):
    sol = [['x']]
    print('Test 2: PASSED' if groupAnagrams(strs) == sol else 'Test 2: FAILED')
    
def test3(strs:list[str] = ['']):
    sol = [['']]
    print('Test 3: PASSED' if groupAnagrams(strs) == sol else 'Test 3: FAILED')
    
test1()
test2()
test3()