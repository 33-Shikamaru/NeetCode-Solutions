'''
Problem: Valid Palindrome
-------

Given a string `s`, return `true` if it is a palindrome, otherwise return `false`.

A palindrome is a string that reads the same forward and backward. It is also
case-insensitive and ignores all non-alphanumeric characters.

Note: Alphanumeric characters consist of letters `(A-Z, a-z)` and numbers `(0-9)`.

-------
URL: https://neetcode.io/problems/is-palindrome?list=neetcode150
'''

def isPalindrome(s: str) -> bool:
    # We can use two pointers and compare the chars to each other and see if they
    # are the same. We use the alnum() function to check if the char is a valid
    # alphanumeric character.
    
    left, right = 0, len(s) - 1
    while left < right:
        # while left < right and not isalphanum(s[left]):
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1
        if s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1
    return True
    
    
    
def test1(s: str = "Was it a car or a cat I saw?"):
    sol = True
    print('Test 1: PASSED' if isPalindrome(s) == sol else 'Test 1: FAILED')
    
def test2(s: str = "tab a cat"):
    sol = False
    print('Test 2: PASSED' if isPalindrome(s) == sol else 'Test 2: FAILED')
    
test1()
test2()