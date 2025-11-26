"""
Problem: Permutation in String
-------

You are given two strings `s1` and `s2`.

Return `True` if `s2` contains a permutation of `s1`, or `False` otherwise. That means
if a permutation of `s1` exists as a substring of `s2`, then return `True`.

Both strings only contain lowercase letters.

-------
URL: https://neetcode.io/problems/buy-and-sell-crypto?list=neetcode150
"""

def permutation_in_string(s1, s2) -> bool:
    # We want to build a table of possible chars (a-z) and keep a count for each s1 and s2.
    # We initially build s1 entirely and only partially build s2 of size len(s1).
    # From this, we have created a sliding window of size len(s1) where we can slide as
    # we iterate through s2, remving and adding chars to s2_char_count. If the two tables
    # ever equal, we know a permutation exists.

    if len(s1) > len(s2):
        return False

    s1_char_count = [0] * 26
    s2_char_count = [0] * 26

    for i in range(len(s1)):
        s1_char_count[ord(s1[i]) - ord("a")] += 1
        s2_char_count[ord(s2[i]) - ord("a")] += 1

    for i in range(len(s1), len(s2)):
        if s1_char_count == s2_char_count:
            return True
        s2_char_count[ord(s2[i - len(s1)]) - ord("a")] -= 1
        s2_char_count[ord(s2[i]) - ord("a")] += 1

    return s1_char_count == s2_char_count


def test1(s1="abc", s2="lecabee"):
    assert permutation_in_string(s1, s2)
    print("Test 1: PASSED")

def test2(s1="abc", s2="lecabee"):
    assert permutation_in_string(s1, s2)
    print("Test 2: PASSED")

def test3(s1="abc", s2="letabee"):
    assert not permutation_in_string(s1, s2)
    print("Test 3: PASSED")

def sample_test():
    assert not permutation_in_string("ab", "eidboaoo")
    print("Sample Test: PASSED")


test1()
test2()
test3()
sample_test()