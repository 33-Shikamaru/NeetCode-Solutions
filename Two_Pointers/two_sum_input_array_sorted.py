'''
Problem: Two Integer Sum II
-------

Given an array of integers `numbers` that is sorted in non-decreasing order.

Return the indicied (1-indexed) of two numbers, `[index1, index2]`, such that 
they add up to a given target number `target` and `index1 < index2`.
Note that `index1` and `index2` cannot be equal, therefore you may not use 
the same element twice.

There will always be one valid solution.

Your solution must use O(1) additional space.

-------
URL: https://neetcode.io/problems/two-integer-sum-ii?list=neetcode150
'''

def twoSum(numbers: list[int], target: int) -> list[int]:
    # The thought process is that we want to get a sum of the two end integers 
    # of the numbers list. We compare this value with the target value and move
    # a pointer based on the comparison. If the value is less, we can increment
    # since the array is sorted. If the value is greater, we can decrement since
    # the array is sorted.
    
    left, right = 0, len(numbers) - 1
    while left < right:
        curr_total = numbers[left] + numbers[right]
        if curr_total == target:
            return [left + 1, right + 1]
        elif curr_total < target:
            left += 1
        else:
            right -= 1
    return []



def test1(numbers: list[int] = [1,2,3,4], target: int = 3):
    sol = [1,2]
    print('Test 1: PASSED' if twoSum(numbers, target) == sol else 'Test 1: FAILED')
    
test1()