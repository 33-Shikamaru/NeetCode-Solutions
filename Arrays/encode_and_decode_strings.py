from collections import defaultdict

'''
Problem: Encode and Decode Strings
-------

Design an algorithm to encode a list of strings to a single string. The encoded string 
is then decoded back to the original list of strings.

Please implement `encode` and `decode`.

-------
URL: https://neetcode.io/problems/string-encode-and-decode?list=neetcode150
'''

# NOTE: This definately can be refactored at some point in time.

def encode(strs: list[str]) -> str:
    # Create a string with an arbitrary structure such that it is easily decodeable.
    # For this case, we use a format of !split!. For complex lists, we could easily
    # extend this "key" such that the occurence of that "key" in the `strs` list
    # would be infinitely small.
    
    if strs == []:
        return ''
    elif strs == [""]:
        return '!empty!'
    return '!split!'.join(strs)
    
def decode(s: str) -> list[str]:
    # Since we know the encoding, we can easily break it apart by the unique "key".
    
    if s == '':
        return []
    elif s == '!empty!':
        return [""]
    return s.split('!split!')


    
def test1(strs:list[str] = ["neet","code","love","you"]):
    sol = ["neet","code","love","you"]
    print('Test 1: PASSED' if decode(encode(strs)) == sol else 'Test 1: FAILED')
    
def test2(strs:list[str] = ["we","say",":","yes"]):
    sol = ["we","say",":","yes"]
    print('Test 2: PASSED' if decode(encode(strs)) == sol else 'Test 2: FAILED')
    
test1()
test2()