'''
Problem: Longest Substring Without Repeating Characters
-------

Given a string `s`, find the length of the longest substring without duplicate characters.

A substring is a contiguous sequence of characters within a string.

-------
URL: https://neetcode.io/problems/longest-substring-without-duplicates?list=neetcode150
'''

def lengthOfLongestSubstring(s: str) -> int:
    # We want to create a hash set to keep track of characters in the current substring by using
    # the two pointer approach. If we find a duplicate, we move the leftmost pointer to the right 
    # 1 space and continue the substring from there. We take the max as we go to ensure we find 
    # the longest substring without repeating characters.
    
    sol = 0
    left = 0
    hash_set = set()
    
    for right in range(len(s)):
        while s[right] in hash_set:
            hash_set.remove(s[left])
            left += 1
        hash_set.add(s[right])
        sol = max(sol, len(hash_set))
    return sol
    
    
def test1(s: str = 'zxyzxyz'):
    sol = 3
    print('Test 1: PASSED' if lengthOfLongestSubstring(s) == sol else 'Test 1: FAILED')
    
def test2(s: str = 'xxxx'):
    sol = 1
    print('Test 2: PASSED' if lengthOfLongestSubstring(s) == sol else 'Test 2: FAILED')
    
test1()
test2()