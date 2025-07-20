'''
Problem: Longest Consecutive Sequence
-------

Given an array of integers `nums`, return the length of the longest consecutive sequence 
of elements that can be formed.

A consecutive sequence is a sequence of elements in which each element is exactly `1` greater 
than the previous element. The elements do not have to be consecutive in the original array.

You must write an algorithm that runs in `O(n)` time.

-------
URL: https://neetcode.io/problems/longest-consecutive-sequence?list=neetcode150
'''

def longestConsecutive(nums: list[int]) -> int:
    # We create a hash set to quickly search if a digit exists in the original list.
    # Then, we only iterate through the digits that could possible exist (min and max values).
    # We would then count the streaks we are on and return that largest possible
    # streak found from the list given.
    
    if not nums:
        return 0
    hash_set = set(nums)
    start, end = min(nums), max(nums)
    sol = -1
    count = 0
    for i in range(start, end + 2): # Want to check a bit past in case we end on a streak
        if i in hash_set:
            count += 1
        else:
            sol = max(count, sol)
            count = 0
    return sol
    

    
def test1(nums: list[int] = [2,20,4,10,3,4,5]):
    sol = 4
    print('Test 1: PASSED' if longestConsecutive(nums) == sol else 'Test 1: FAILED')
    
def test2(nums: list[int] = [0,3,2,5,4,6,1,1]):
    sol = 7
    print('Test 2: PASSED' if longestConsecutive(nums) == sol else 'Test 2: FAILED')
    
test1()
test2()