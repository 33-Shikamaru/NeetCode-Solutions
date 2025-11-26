'''
Problem: Minimum Window Substring
-------

Given two strings `s` and `t`, return the shortest substring of `s` such that every character in
`t`, included duplicates, is present in the substring. If such a substring does not exist, return
an empty string `""`.

You may assume that the correct output is always unique.

-------
URL: https://neetcode.io/problems/minimum-window-with-characters/question?list=neetcode150
'''
from collections import defaultdict


def minimumWindowSubstring(s: str, t: str) -> str:
    # We want to build a sliding window that contains all characters in t
    # by adding seen characters to a window dictionary that we compare to
    # the target dictionary `t_count`. We further optimize by keeping track
    # of current `have` and `need` counts to minimize repetitive computations.

    if t == '':
        return ''

    t_count, window = defaultdict(int), defaultdict(int)
    for ch in t:
        t_count[ch] += 1

    have, need = 0, len(t_count)
    result, result_length = [-1, -1], float("infinity")
    left = 0
    for right in range(len(s)):
        curr_char = s[right]
        window[curr_char] += 1

        if curr_char in t_count and window[curr_char] == t_count[curr_char]:
            have += 1

        while have == need:
            if (right - left + 1) < result_length:
                result = [left, right]
                result_length = right - left + 1

            window[s[left]] -= 1
            if s[left] in t_count and window[s[left]] < t_count[s[left]]:
                have -= 1
            left += 1
    left, right = result

    return s[left:right + 1] if result_length != float("infinity") else ''

def test1(s: str = "OUZODYXAZV", t: str = "XYZ"):
    assert minimumWindowSubstring(s, t) == "YXAZ"
    print("Test 1: PASSED")

def test2(s: str = "xyz", t: str = "xyz"):
    assert minimumWindowSubstring(s, t) == "xyz"
    print("Test 2: PASSED")

def test3(s: str = "x", t: str = "xy"):
    assert minimumWindowSubstring(s, t) == ""
    print("Test 3: PASSED")

test1()
test2()
test3()
