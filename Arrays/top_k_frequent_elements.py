from collections import Counter
'''
Problem: Top K Frequent Elements
-------

Given an integer arrays `nums` and an integer `k`, return the `k`
most frequent elements within the array.

The test cases are generated such that the answer is always **unique**.


-------
URL: https://neetcode.io/problems/top-k-elements-in-list?list=neetcode150
'''

def topKFrequent(nums: list[int], k: int) -> list[int]:
    # Creates a dict-type container for all values in nums, then as we pop off
    # the top K frequent elements such that we can have them return in freq order. 
    
    counts = Counter(nums)
    sol = []
    for i in range(k):
        value = counts.most_common()[0][0]
        del counts[value]
        sol.append(value)
    return sol

    
def test1(nums: list[int] = [1,2,2,3,3,3], k = 2):
    sol = [2,3]
    print('Test 1: PASSED' if sorted(topKFrequent(nums, k)) == sol else 'Test 1: FAILED')
    
def test2(nums: list[int] = [7,7], k = 1):
    sol = [7]
    print('Test 2: PASSED' if topKFrequent(nums, k) == sol else 'Test 2: FAILED')
    
test1()
test2()