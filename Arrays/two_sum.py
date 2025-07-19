'''
Problem: Two Sum
-------

Given an array of integers `nums` and an integer `target`, return the indices `i` and `j`
such that `nums[i] + nums[j] == target` and `i != j`.

You may assume that every input has exactly one pair of indices `i` and `j` that
satisfy the condition.

Return the answer with the smaller index first.

-------
URL: https://neetcode.io/problems/two-integer-sum?list=neetcode150
'''

def twoSum(nums: list[int], target: int ) -> list[int]:
    # We can build the hash table in one pass by using the enumerate function
    # to gather the index of a value in the nums list. We then insert each value 
    # into the hash map and check if the remainder (to get to our target value) 
    # exists. Once it does, we can retrieve that value's index from the hash
    # table and pair it with our current index, then return that as a list.
    
    hash_table = {}
    for index, num in enumerate(nums):
        if target - num in hash_table:
            return [hash_table[target - num], index]
        hash_table[num] = index
    return []
            

    
def test1(nums:list[int] = [3,4,5,6], target: int = 7):
    sol = [0,1]
    print('Test 1: PASSED' if twoSum(nums, target) == sol else 'Test 1: FAILED')
    
def test2(nums:list[int] = [4,5,6], target: int = 10):
    sol = [0,2]
    print('Test 2: PASSED' if twoSum(nums, target) == sol else 'Test 2: FAILED')
    
def test3(nums:list[int] = [5,5], target: int = 10):
    sol = [0,1]
    print('Test 3: PASSED' if twoSum(nums, target) == sol else 'Test 3: FAILED')
    
test1()
test2()
test3()