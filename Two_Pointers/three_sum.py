'''
Problem: 3 Sum
-------

Given an integer array `nums`, return all the triplets `nums[i], nums[j], nums[k]]`
where `nums[i] + nums[j] + nums[k] == 0`, and the indices `i`, `j`, `k` are distinct.

The output should not contain any duplicate triplets. You may return the output and the
triplets in any order.

-------
URL: https://neetcode.io/problems/three-integer-sum?list=neetcode150
'''

def threeSum(nums: list[int]) -> list[list[int]]:
    # We can iterate through each character in the nums list and we
    # can use the same two pointer approach to find the triplets in 
    # each pass. We then just return the set of unique triplets.
    
    nums.sort()
    sol = []
    n = len(nums)
    for i in range(n):
        left = i + 1
        right = n - 1
        while left < right:
            curr_total = nums[i] + nums[left] + nums[right]
            if curr_total > 0:
                right -= 1
            elif curr_total < 0:
                left += 1
            else:
                pairs = [nums[i], nums[left], nums[right]]
                if pairs not in sol:
                    sol.append(pairs)
                left += 1
                right -= 1
    return sol
    
    
    
def test1(nums: list[int] = [-1,0,1,2,-1,-4]):
    sol = [[-1,-1,2],[-1,0,1]]
    print('Test 1: PASSED' if threeSum(nums) == sol else 'Test 1: FAILED')
    
def test2(nums: list[int] = [0,1,1]):
    sol = []
    print('Test 2: PASSED' if threeSum(nums) == sol else 'Test 2: FAILED')
    
def test3(nums: list[int] = [0,0,0]):
    sol = [[0,0,0]]
    print('Test 3: PASSED' if threeSum(nums) == sol else 'Test 3: FAILED')
    
test1()
test2()
test3()